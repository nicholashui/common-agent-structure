from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(25000)
        page.goto(f"{BASE}/", wait_until="domcontentloaded")
        page.wait_for_timeout(600)
        body = page.locator("body").inner_text()
        print("fleet_pack_browser", "Pack browser" in body or "not a swarm runner" in body.lower())
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat-log]", timeout=20000)
        honesty = page.locator("[data-testid=project-chat-honesty]").inner_text()
        print("honesty", honesty)
        print("assembled_header", "Host" in page.locator("[data-testid=project-chat-output-header]").inner_text())
        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        wf = page.locator("[data-testid=project-flow]").inner_text()
        print("pack_map_chip", "pack map" in wf.lower())
        print("planner_next_hidden", page.locator("[data-testid^=project-next-]").count() == 0)
        page.locator('[data-testid="project-open-chat-agent-video-promptengineer"]').click()
        page.wait_for_timeout(800)
        print("workflow_click_chat", "/chat" in page.url and "/projects/asain-beauty" in page.url)
        print("workflow_not_profile", "/agents/" not in page.url)
        page.goto(f"{BASE}/agents/video.promptengineer/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=agent-chat-not-autopilot]", timeout=15000)
        print("profile_badge", page.locator("[data-testid=agent-chat-not-autopilot]").inner_text())
        browser.close()


if __name__ == "__main__":
    main()
