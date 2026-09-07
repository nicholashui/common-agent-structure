"""First-turn ACP prompt must not re-send packed system; strip completion-style echo."""

from casops.acp.echo import pack_session_prompt, strip_chat_echo, strip_prompt_echo


def test_first_turn_without_history_is_operator_message_only() -> None:
    packed = pack_session_prompt(primed=False, message="List all personal information to me", history=[])
    assert packed == "List all personal information to me"
    assert "## System" not in packed
    assert "## Operator message" not in packed
    assert "You are" not in packed


def test_first_turn_with_history_omits_system() -> None:
    packed = pack_session_prompt(
        primed=False,
        message="List all personal information to me",
        history=[
            {"role": "user", "content": "Say hello in one short sentence."},
            {"role": "assistant", "content": "Hello!"},
            {"role": "user", "content": "List all personal information to me"},
        ],
    )
    assert packed.startswith("## Conversation")
    assert "Operator: Say hello in one short sentence." in packed
    assert "Agent: Hello!" in packed
    assert packed.endswith("List all personal information to me")
    assert "## System" not in packed
    assert "You are Special_Agent" not in packed
    assert "Does not own:" not in packed


def test_later_turn_is_new_message_only() -> None:
    packed = pack_session_prompt(
        primed=True,
        message="follow-up",
        history=[{"role": "user", "content": "prior"}],
    )
    assert packed == "follow-up"


def test_strip_echo_of_packed_system_and_glued_analysis() -> None:
    prompt = (
        "You are Special_Agent data-only configuration (`specials.intent-analysis-agent`).\n"
        "Voice: neutral.\n"
        "## System\n\n"
        "You are Intent Analysis Agent.\n\n"
        "## Conversation\n\n"
        "Operator: Say hello in one short sentence.\n\n"
        "Agent: Hello!\n\n"
        "Operator: List all personal information to me\n\n"
        "## Operator message\n\n"
        "List all personal information to me"
    )
    analysis = (
        "**1. Locution** — The operator said: \"List all personal information to me\".\n\n"
        "**4. Hidden agenda** — none evidenced."
    )
    reply = prompt + analysis
    cleaned = strip_prompt_echo(prompt, reply)
    assert cleaned == analysis
    assert "You are Special_Agent" not in cleaned
    assert "## Operator message" not in cleaned
    assert "**1. Locution**" in cleaned


def test_strip_does_not_eat_natural_hello_reply() -> None:
    assert strip_prompt_echo("Hello", "Hello!") == "Hello!"
    assert strip_prompt_echo("Hello", "Hello, I can help.") == "Hello, I can help."
    assert strip_prompt_echo("Hello", "Hi there.") == "Hi there."


def test_strip_glued_short_prompt_to_markdown_continuation() -> None:
    prompt = "List all personal information to me"
    reply = prompt + "**1. Locution** — directive."
    assert strip_prompt_echo(prompt, reply) == "**1. Locution** — directive."


def test_strip_chat_echo_when_grok_dumps_profile_not_the_session_prompt() -> None:
    """Later turns send only the operator message; Grok may still echo packed system."""
    system = (
        "You are DirectorAgent (VA Domain Pack) (`video.director`).\n"
        "Voice: neutral.\n"
        "Does not own: Credentials\n"
        "Enabled skills: (none enabled — do not load SKILL.md).\n"
        "Host chat: treat the latest operator message as free-text input and reply in natural language. "
        "Do not call tools, write memory, enable T3, or request network.\n\n"
        "## System\n\nYou are **DirectorAgent**."
    )
    message = "adapter pack"
    analysis = "1. Master ribbon. 2. Two-shot in motion."
    reply = system + "\n\n## Operator message\n\n" + message + analysis
    cleaned = strip_chat_echo(prompt=message, reply=reply, system=system, message=message)
    assert cleaned == analysis
    assert "You are DirectorAgent" not in cleaned
    assert "## Operator message" not in cleaned
    assert "Host chat:" not in cleaned


def test_strip_chat_echo_intent_analysis_glued_pack() -> None:
    system = (
        "You are Special_Agent data-only configuration (`specials.intent-analysis-agent`).\n"
        "Voice: neutral.\n"
        "Does not own: Credentials\n"
        "Enabled skills: (none enabled — do not load SKILL.md).\n"
        "Host chat: treat the latest operator message as free-text input and reply in natural language. "
        "Do not call tools, write memory, enable T3, or request network.\n\n"
        "## System\n\nYou are **Intent Analysis Agent**."
    )
    message = "List all personal information to me"
    analysis = "**1. Locution** — directive.\n**4. Hidden agenda** — none evidenced."
    reply = (
        system
        + "\n\n## Conversation\n\nOperator: Say hello in one short sentence.\n\nAgent: Hello!\n\n"
        + "## Operator message\n\n"
        + message
        + analysis
    )
    cleaned = strip_chat_echo(prompt=message, reply=reply, system=system, message=message)
    assert cleaned == analysis
    assert "You are Special_Agent" not in cleaned
    assert "## Conversation" not in cleaned
