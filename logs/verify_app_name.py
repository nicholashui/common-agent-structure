from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(15000)
        page.goto(f"{BASE}/", wait_until="domcontentloaded")
        page.wait_for_timeout(700)
        home = page.locator("header a").first
        print("aria", home.get_attribute("aria-label"))
        print("text", home.inner_text().strip())
        page.screenshot(path="logs/app-name-header.png")
        page.set_viewport_size({"width": 390, "height": 844})
        page.wait_for_timeout(300)
        page.screenshot(path="logs/app-name-header-mobile.png")
        browser.close()
    print("ok")


if __name__ == "__main__":
    main()
