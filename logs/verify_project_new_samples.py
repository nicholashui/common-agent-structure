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
        print("study_row", page.locator("[data-testid=project-study-samples]").count())
        print("chip_asain", page.locator("[data-testid=project-study-asain-beauty]").count())
        print("chip_european", page.locator("[data-testid=project-study-european-handsome]").count())
        print("chip_jp", page.locator("[data-testid=project-study-japanese-grandma-gta]").count())
        print("chip_hk", page.locator("[data-testid=project-study-hongkong-grandma-gta]").count())
        print("name_ph", page.locator("[data-testid=project-name]").get_attribute("placeholder"))
        print("title_ph", page.locator("[data-testid=project-title]").get_attribute("placeholder"))
        print("brief_ph", page.locator("[data-testid=project-brief]").get_attribute("placeholder"))
        print("audience_ph", page.locator("[data-testid=project-audience]").get_attribute("placeholder"))
        print("notes_ph", page.locator("[data-testid=project-notes]").get_attribute("placeholder"))
        print("no_safety", "safety-recap" not in (page.locator("[data-testid=project-name]").get_attribute("placeholder") or ""))
        page.fill("[data-testid=project-name]", "my-clip")
        page.locator("[data-testid=project-study-european-handsome]").click()
        page.wait_for_timeout(200)
        print("name_kept", page.locator("[data-testid=project-name]").input_value())
        print("title_filled", page.locator("[data-testid=project-title]").input_value())
        print("brief_filled", page.locator("[data-testid=project-brief]").input_value())
        print("audience_filled", page.locator("[data-testid=project-audience]").input_value())
        print("duration_filled", page.locator("[data-testid=project-duration]").input_value())
        print("notes_filled", page.locator("[data-testid=project-notes]").input_value())
        page.locator("[data-testid=project-study-hongkong-grandma-gta]").click()
        page.wait_for_timeout(200)
        print("brief_hk", page.locator("[data-testid=project-brief]").input_value())
        print("name_still", page.locator("[data-testid=project-name]").input_value())
        page.screenshot(path="logs/project-new-study-desktop.png")
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/new", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-study-samples]", timeout=20000)
        print("mobile_chips", page.locator("[data-testid=project-study-samples] button").count())
        page.screenshot(path="logs/project-new-study-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
