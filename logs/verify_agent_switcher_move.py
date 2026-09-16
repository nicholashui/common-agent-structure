from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"


def count_switcher(page):
    return page.locator("#agent-switcher").count()


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(20000)

        page.goto(f"{BASE}/", wait_until="domcontentloaded")
        page.wait_for_timeout(800)
        print("home_switcher", count_switcher(page))
        page.screenshot(path="logs/agent-switcher-home.png")

        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(800)
        print("project_chat_switcher", count_switcher(page))

        page.goto(f"{BASE}/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(600)
        print("workflow_switcher", count_switcher(page))

        page.goto(f"{BASE}/agents/video.promptengineer", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=agent-profile-switcher]", timeout=15000)
        print("overview_switcher", count_switcher(page))
        print("overview_placeholder", page.locator("#agent-switcher").get_attribute("placeholder"))
        page.screenshot(path="logs/agent-switcher-overview.png")

        page.goto(f"{BASE}/agents/video.promptengineer/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=agent-chat]", timeout=15000)
        print("chat_switcher", count_switcher(page))
        page.locator("#agent-switcher").click()
        page.wait_for_selector("#agent-switcher-list", timeout=5000)
        page.locator("#agent-switcher-list button", has_text="video.director").first.click()
        page.wait_for_timeout(800)
        print("after_switch_url", page.url)
        print("after_switch_placeholder", page.locator("#agent-switcher").get_attribute("placeholder"))
        page.screenshot(path="logs/agent-switcher-chat.png")

        page.goto(f"{BASE}/agents/video.director/files", wait_until="domcontentloaded")
        page.wait_for_timeout(800)
        print("files_switcher", count_switcher(page))

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/", wait_until="domcontentloaded")
        page.wait_for_timeout(600)
        print("mobile_home_switcher", count_switcher(page))
        page.screenshot(path="logs/agent-switcher-home-mobile.png")
        page.goto(f"{BASE}/agents/video.promptengineer/structure", wait_until="domcontentloaded")
        page.wait_for_timeout(800)
        print("mobile_structure_switcher", count_switcher(page))
        page.screenshot(path="logs/agent-switcher-structure-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
