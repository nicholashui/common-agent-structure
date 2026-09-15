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

        page.goto(f"{BASE}/projects/new", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-new]", timeout=20000)
        page.wait_for_timeout(400)
        print("no_study_row", page.locator("[data-testid=project-study-samples]").count())
        print("no_save_until_rank", page.locator("[data-testid=project-save]").count())
        print("name_ph", page.locator("[data-testid=project-name]").get_attribute("placeholder"))
        print("brief_ph", page.locator("[data-testid=project-brief]").get_attribute("placeholder"))
        print("save_hint", "Save is below" in page.inner_text("[data-testid=project-new]"))
        page.screenshot(path="logs/project-new-save-desktop.png")

        page.goto(f"{BASE}/projects/asain-beauty/start", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-start]", timeout=20000)
        page.wait_for_timeout(600)
        print("start_page", page.locator("[data-testid=project-start]").count())
        print("start_name", page.locator("[data-testid=project-name]").input_value())
        print("start_brief", page.locator("[data-testid=project-brief]").input_value())
        print("start_name_ro", page.locator("[data-testid=project-name]").get_attribute("readonly"))
        print("start_no_save", page.locator("[data-testid=project-save]").count())
        print("crumb", page.locator("[data-testid=page-location]").inner_text())
        page.screenshot(path="logs/project-start-asain-desktop.png")

        page.locator("[data-testid=nav-project]").click()
        page.wait_for_timeout(200)
        page.locator("[data-testid=nav-project-asain-beauty-toggle]").click()
        page.wait_for_timeout(200)
        print("nav_start", page.locator("[data-testid=nav-project-asain-beauty-start]").count())
        print("nav_workflow", page.locator("[data-testid=nav-project-asain-beauty-workflow]").count())
        print("nav_chat", page.locator("[data-testid=nav-project-asain-beauty-chat]").count())

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/european-handsome/start", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-start]", timeout=20000)
        print("mobile_title", page.locator("[data-testid=project-title]").input_value())
        page.screenshot(path="logs/project-start-european-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
