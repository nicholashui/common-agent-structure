import os
import re
import time
import sys
import random
import argparse
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    print("Installing python-dotenv...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv"])
    from dotenv import load_dotenv

try:
    import requests
except ImportError:
    print("Installing requests...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

from llm import ENV_PATH, add_llm_args, complete, resolve_llm


BASE_DIR = Path(__file__).resolve().parent
SEPARATOR = "<#0.5#>"


def parse_args():
    p = argparse.ArgumentParser(
        description="Translate a markdown book into a Cantonese voice-over script (HK).")
    p.add_argument(
        "-i", "--input",
        required=True,
        help="input markdown file",
    )
    p.add_argument(
        "-o", "--output",
        required=True,
        help="output script file",
    )
    p.add_argument(
        "-p", "--prompt",
        required=True,
        help="system prompt file (e.g. ytscript.txt)",
    )
    add_llm_args(p)
    return p.parse_args()


def resolve_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = Path.cwd() / path
    return path.resolve()


def load_dotenv_file():
    if not ENV_PATH.is_file():
        raise FileNotFoundError(f"dotenv file not found: {ENV_PATH}")
    load_dotenv(dotenv_path=ENV_PATH)


def load_system_prompt(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"System prompt file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def extract_transition_words(system_prompt):
    in_code_block = False
    code_content = []
    for line in system_prompt.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
            else:
                in_code_block = False
            continue
        if in_code_block:
            code_content.append(line)
    block = "".join(code_content)
    raw = [t.strip() for t in re.split(r"[／／、,，]", block) if t.strip()]
    seen = set()
    cleaned = []
    for w in raw:
        w = w.strip("。.！!？?；;：:\"'` ")
        if w and w not in seen:
            seen.add(w)
            cleaned.append(w)
    if not cleaned:
        cleaned = ["跟住我哋講嘅係", "好啦", "然後", "另外", "最後"]
    return cleaned


def build_transition_instruction(transition_words, section_index, total_sections):
    pool = list(transition_words)
    random.shuffle(pool)
    num_for_opening = 1
    num_for_mid = min(6, max(3, len(pool) // 4))
    opening = pool[:num_for_opening]
    remaining = pool[num_for_opening:]
    if len(remaining) < num_for_mid:
        random.shuffle(pool)
        mid_pool = pool[:num_for_mid]
    else:
        mid_pool = remaining[:num_for_mid]
    random.shuffle(mid_pool)

    open_str = "、".join(opening)
    mid_str = "、".join(mid_pool)
    instruction = (
        f"\n\n【本節隨機抽選過場字指令 — 必須嚴格遵守，唔可以用其他】\n"
        f"呢一節係第 {section_index}/{total_sections} 節，系統已經幫你隨機抽好要用嘅過場字，"
        f"你只可以用以下指定嘅字，絕對唔可以用列表入面其他過場字：\n"
        f"・開頭一定要用：【{open_str}】 或者由開頭變化出嚟嘅同義句式\n"
        f"・中間過渡可以用：【{mid_str}】\n"
        f"・嚴禁再用「跟住我哋講嘅係」除非佢出現喺上面指定列表入面\n"
        f"・每次過渡都要轉另一個字，唔好重複用同一個\n"
    )
    return instruction, opening, mid_pool


def load_markdown(path):
    if not path.exists():
        raise FileNotFoundError(f"Markdown file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_markdown_by_headings(md_text):
    lines = md_text.splitlines(keepends=True)
    heading_re = re.compile(r"^(#{1,6})\s+(.+)$")

    sections = []
    current_lines = []
    current_heading = None

    for line in lines:
        m = heading_re.match(line.rstrip("\n").rstrip("\r"))
        if m:
            if current_lines:
                if current_heading is not None or any(l.strip() for l in current_lines):
                    sections.append("".join(current_lines).rstrip())
            current_lines = [line]
            current_heading = m.group(2)
        else:
            current_lines.append(line)

    if current_lines:
        if current_heading is not None or any(l.strip() for l in current_lines):
            sections.append("".join(current_lines).rstrip())

    non_empty = []
    for s in sections:
        if s.strip():
            non_empty.append(s)
    return non_empty


def main():
    args = parse_args()
    input_path = resolve_path(args.input)
    output_path = resolve_path(args.output)
    prompt_path = resolve_path(args.prompt)
    print(f"Input:  {input_path}")
    print(f"Output: {output_path}")
    print(f"Prompt: {prompt_path}")
    print(f"Env:    {ENV_PATH}")

    print("Loading environment...")
    load_dotenv_file()
    client = resolve_llm(args.llm, args.model)
    print(f"LLM: {client.provider} ({client.label})")
    print(f"Model: {client.model}")
    print(f"Base: {client.base_url}")

    print("Loading system prompt...")
    system_prompt = load_system_prompt(prompt_path)
    print(f"System prompt length: {len(system_prompt)} chars")

    print("Extracting transition words...")
    transition_words = extract_transition_words(system_prompt)
    print(f"Found {len(transition_words)} transition words:")
    print(f"  {', '.join(transition_words)}")

    print("Loading markdown...")
    md_text = load_markdown(input_path)
    print(f"Markdown length: {len(md_text)} chars")

    print("Splitting by headings...")
    sections = split_markdown_by_headings(md_text)
    print(f"Found {len(sections)} sections")
    for i, s in enumerate(sections):
        first_line = s.splitlines()[0][:80] if s.splitlines() else "(empty)"
        print(f"  [{i+1}] {len(s)} chars - {first_line}")

    print("\nTranslating sections (this may take a while)...")
    results = []
    for i, section in enumerate(sections):
        sidx = i + 1
        total = len(sections)
        trans_instr, opening, mid_pool = build_transition_instruction(transition_words, sidx, total)
        print(f"\nProcessing section {sidx}/{total} ({len(section)} chars)...")
        print(f"  Random opening: 「{' / '.join(opening)}」")
        print(f"  Random mid:     「{' / '.join(mid_pool)}」")
        enriched_user_content = section + trans_instr
        try:
            translated = complete(
                client, system_prompt, enriched_user_content, temperature=0.7, timeout=300
            )
            results.append(translated)
            print(f"  Translated: {len(translated)} chars")
            first_preview = translated[:120].replace("\n", " ")
            print(f"  Preview: {first_preview}...")
        except Exception as e:
            print(f"  ERROR on section {sidx}: {e}")
            fallback = f"[Translation failed for section {sidx}: {e}]"
            results.append(fallback)
        time.sleep(1)

    print(f"\nCombining {len(results)} sections with separator '{SEPARATOR}'...")
    output = SEPARATOR.join(results)

    print(f"Writing output to {output_path}...")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Done! Output written to {output_path}")
    print(f"Total output length: {len(output)} chars")


if __name__ == "__main__":
    main()
