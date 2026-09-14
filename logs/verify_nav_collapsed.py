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
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=nav-project]", timeout=20000)
        page.wait_for_timeout(500)
        print("project_expanded", page.locator("[data-testid=nav-project]").get_attribute("aria-expanded"))
        print("workflow_expanded", page.locator("[data-testid=nav-agent-workflow]").get_attribute("aria-expanded"))
        print("agent_expanded", page.locator("[data-testid=nav-agent-profile]").get_attribute("aria-expanded"))
        print("new_project", page.locator("[data-testid=nav-project-new]").count())
        print("asain_row", page.locator("[data-testid=nav-project-asain-beauty]").count())
        print("asain_workflow", page.locator("[data-testid=nav-project-asain-beauty-workflow]").count())
        page.locator("[data-testid=nav-project]").click()
        page.wait_for_timeout(200)
        print("after_project_click_expanded", page.locator("[data-testid=nav-project]").get_attribute("aria-expanded"))
        print("after_new_project", page.locator("[data-testid=nav-project-new]").count())
        print("after_asain_row", page.locator("[data-testid=nav-project-asain-beauty]").count())
        print("after_asain_chat", page.locator("[data-testid=nav-project-asain-beauty-chat]").count())
        print("workflow_still_closed", page.locator("[data-testid=nav-agent-workflow]").get_attribute("aria-expanded"))
        page.screenshot(path="logs/nav-all-collapsed-desktop.png")
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/european-handsome/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(600)
        page.locator("button[aria-label='Open navigation']").click()
        page.wait_for_selector("[data-testid=nav-project]", timeout=10000)
        print("mobile_project_expanded", page.locator("[data-testid=nav-project]").get_attribute("aria-expanded"))
        print("mobile_new_project", page.locator("[data-testid=nav-project-new]").count())
        page.screenshot(path="logs/nav-all-collapsed-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
