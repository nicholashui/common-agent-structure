from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"


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
        page.locator("[data-testid=nav-program]").click()
        page.wait_for_timeout(300)
        print("new_link", page.locator("[data-testid=nav-program-new]").count())
        labels = page.locator("nav").inner_text()
        print("program_above_project", labels.find("Program") < labels.find("Project") and "Program" in labels)
        page.locator("[data-testid=nav-program-new]").click()
        page.wait_for_selector("[data-testid=program-new]", timeout=10000)
        print("crumb", page.locator("[data-testid=page-location]").inner_text())
        print("code_field", page.locator("[data-testid=program-code]").count())
        print("name_field", page.locator("[data-testid=program-name]").count())
        page.locator("[data-testid=program-code]").fill("Spring Launch")
        print("code_normalized", page.locator("[data-testid=program-code]").input_value())
        page.screenshot(path="logs/program-new.png")
        page.set_viewport_size({"width": 390, "height": 844})
        page.locator("button[aria-label='Open navigation']").click()
        page.wait_for_timeout(300)
        page.screenshot(path="logs/program-nav-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
