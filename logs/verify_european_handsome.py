from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"
ROLES = [
    "video.promptengineer",
    "video.director",
    "video.cinematographer",
    "video.mua_makeup",
    "video.continuity",
]
PROBE = "A few teeth may flash and disappear."


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(25000)

        page.goto(f"{BASE}/projects", wait_until="domcontentloaded")
        page.wait_for_timeout(800)
        listing = page.content()
        print("projects_list_has_european", "european-handsome" in listing)

        page.goto(f"{BASE}/projects/european-handsome/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat-log]", timeout=20000)
        page.wait_for_timeout(900)
        headers = page.locator("[data-testid^=project-chat-header-]").all_text_contents()
        print("n_headers", len(headers))
        joined = "\n".join(headers)
        for role in ROLES:
            print(f"has Human → {role}", f"Human → {role}" in joined)
        print("has cameraoperator human", "Human → video.cameraoperator" in joined)
        print("has critic human", "Human → video.critic" in joined)
        print("has intent", "intent-analysis-agent" in joined)
        print("has creative", "creative-agent" in joined)
        honesty = page.locator("[data-testid=project-chat-honesty]")
        print("honesty", honesty.inner_text() if honesty.count() else "")
        status = page.locator("[data-testid=project-autopilot-status]")
        print("autopilot", status.count(), status.inner_text() if status.count() else "")
        print("open_asks", page.locator("[data-testid=project-human-asks]").count())
        output = page.locator("[data-testid=project-chat-output]")
        print("output_panel", output.count())
        output_text = output.inner_text() if output.count() else ""
        print("output_has_rooftop", "Rooftop phone-macro" in output_text or "rooftop" in output_text.lower())
        print("output_has_scar", "tiny pale scar" in output_text)
        print("output_has_probe", PROBE in output_text)
        print("generator_tags", page.locator("[data-testid=project-generator-tags]").count())
        print("grok_imagine", page.locator("[data-testid=project-generator-grok-imagine]").count())
        print("cycle_gate", page.locator("[data-testid=project-cycle-gate]").count())
        page.screenshot(path="logs/european-handsome-chat-desktop.png")

        page.goto(f"{BASE}/projects/european-handsome/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1800)
        nodes = page.locator("[data-testid=project-agent-node]")
        print("agent_nodes", nodes.count())
        labels = page.locator(".casops-node").all_text_contents()
        print("has_intent_node", any("intent" in t.lower() for t in labels))
        print("has_creative_node", any("creative" in t.lower() for t in labels))
        print("has_output_node", any("output" in t.lower() for t in labels))
        print("has_human_node", any("human" in t.lower() for t in labels))
        print("has_scar_on_graph", any("scar" in t.lower() for t in labels))
        pack = page.locator("text=pack map").first
        print("pack_map_banner", pack.count() > 0)
        chat_btn = page.locator("[data-testid=project-open-chat-agent-video-director]")
        print("chat_button", chat_btn.count())
        if chat_btn.count():
            chat_btn.first.click()
            page.wait_for_url("**/projects/european-handsome/chat**", timeout=10000)
            print("workflow_chat_nav", "/chat" in page.url)
        page.goto(f"{BASE}/projects/european-handsome/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        page.screenshot(path="logs/european-handsome-workflow-desktop.png")

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/european-handsome/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat-log]", timeout=20000)
        page.wait_for_timeout(600)
        print("mobile_headers", page.locator("[data-testid^=project-chat-header-]").count())
        page.screenshot(path="logs/european-handsome-chat-mobile.png")
        page.goto(f"{BASE}/projects/european-handsome/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        page.screenshot(path="logs/european-handsome-workflow-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
