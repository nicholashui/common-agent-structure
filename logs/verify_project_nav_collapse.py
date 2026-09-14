from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"
NAV_KEY = "casops.control-ui.nav.v1"


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(25000)
        page.add_init_script(
            f"localStorage.setItem({NAV_KEY!r}, JSON.stringify({{collapsed:false,agentOpen:true,workflowOpen:true,projectOpen:true,openProjects:[]}}))"
        )
        page.goto(f"{BASE}/projects/new", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=nav-project-asain-beauty]", timeout=20000)
        page.wait_for_timeout(400)
        print("asain_row", page.locator("[data-testid=nav-project-asain-beauty]").count())
        print("european_row", page.locator("[data-testid=nav-project-european-handsome]").count())
        print("asain_workflow_closed", page.locator("[data-testid=nav-project-asain-beauty-workflow]").count())
        print("european_chat_closed", page.locator("[data-testid=nav-project-european-handsome-chat]").count())
        print("asain_expanded", page.locator("[data-testid=nav-project-asain-beauty]").get_attribute("aria-expanded"))
        page.locator("[data-testid=nav-project-asain-beauty-toggle]").click()
        page.wait_for_timeout(200)
        print("asain_workflow_open", page.locator("[data-testid=nav-project-asain-beauty-workflow]").count())
        print("asain_chat_open", page.locator("[data-testid=nav-project-asain-beauty-chat]").count())
        print("european_still_closed", page.locator("[data-testid=nav-project-european-handsome-workflow]").count())
        page.locator("[data-testid=nav-project-asain-beauty-toggle]").click()
        page.wait_for_timeout(200)
        print("asain_workflow_after_collapse", page.locator("[data-testid=nav-project-asain-beauty-workflow]").count())
        page.locator("[data-testid=nav-project-european-handsome]").click()
        page.wait_for_url("**/projects/european-handsome/workflow**", timeout=10000)
        page.wait_for_timeout(400)
        print("title_nav", "/european-handsome/workflow" in page.url)
        print("european_auto_open", page.locator("[data-testid=nav-project-european-handsome-workflow]").count())
        print("asain_independent", page.locator("[data-testid=nav-project-asain-beauty-workflow]").count())
        page.screenshot(path="logs/project-nav-expand-desktop.png")
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(600)
        page.locator("button[aria-label='Open navigation']").click()
        page.wait_for_selector("[data-testid=nav-project-asain-beauty]", timeout=10000)
        print("mobile_asain_open", page.locator("[data-testid=nav-project-asain-beauty-chat]").count())
        print("mobile_european_closed", page.locator("[data-testid=nav-project-european-handsome-chat]").count())
        page.locator("[data-testid=nav-project-european-handsome-toggle]").click()
        page.wait_for_timeout(200)
        print("mobile_european_open", page.locator("[data-testid=nav-project-european-handsome-chat]").count())
        page.screenshot(path="logs/project-nav-expand-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
