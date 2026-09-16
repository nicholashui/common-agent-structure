from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"


def abs_hits(text: str) -> list[str]:
    hits = []
    if "C:\\" in text or "C:/" in text:
        hits.append("drive")
    if "/Users/" in text or "/home/" in text:
        hits.append("posix-home")
    return hits


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(25000)

        page.goto(f"{BASE}/projects/european-handsome/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-flow]", timeout=20000)
        page.wait_for_timeout(800)
        flow = page.locator("[data-testid=project-flow]").inner_text()
        print("workflow_folder_line", [line for line in flow.splitlines() if "project/" in line][:2])
        print("workflow_abs", abs_hits(flow))

        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat-output]", timeout=20000)
        out = page.locator("[data-testid=project-chat-output]").inner_text()
        print("chat_output_paths", [line for line in out.splitlines() if "project/" in line or "spec/" in line][:4])
        print("project_chat_abs", abs_hits(out))

        page.goto(f"{BASE}/agents/video.promptengineer/files", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=files-path]", timeout=20000)
        files_path = page.locator("[data-testid=files-path]").inner_text()
        print("files_path", files_path)
        print("files_abs", abs_hits(page.locator("body").inner_text()))

        page.goto(f"{BASE}/agents", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        fleet = page.locator("body").inner_text()
        print("fleet_abs", abs_hits(fleet))
        print("fleet_has_agents_slash", "agents/" in fleet)

        page.goto(f"{BASE}/agents/video.director/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        chat_files = page.locator("[data-testid=chat-file]").count()
        print("chat_files", chat_files)
        if chat_files:
            sample = page.locator("[data-testid=chat-file]").first.inner_text()
            print("chat_file_sample", sample.replace("\n", " | ")[:240])
            print("chat_file_abs", abs_hits(sample))

        page.screenshot(path="logs/relative-paths-desktop.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
