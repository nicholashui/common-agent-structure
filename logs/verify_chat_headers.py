from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path("logs")
BASE = "http://127.0.0.1:15173"


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(20000)
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        first = page.locator("[data-testid=project-chat-header-comm-0001]")
        print("first header", first.inner_text().replace("\n", " | "))
        second = page.locator("[data-testid=project-chat-header-comm-0002]")
        print("second header", second.inner_text().replace("\n", " | "))
        page.screenshot(path=str(OUT / "chat-header-first.png"))
        pe = page.locator("[data-testid=project-chat-comm-0003]")
        if pe.count() == 0:
            pe = page.locator("[data-testid=project-chat-comm-0003], [data-comm-id=comm-0003]")
        pe.scroll_into_view_if_needed()
        tags = page.locator("[data-testid=project-chat-options-comm-0003] button")
        print("option tags", tags.count())
        if tags.count():
            print("tag0", tags.first.inner_text()[:240].replace("\n", " | "))
            print("check selected", page.locator("[data-testid=project-option-check-1]").count())
        page.screenshot(path=str(OUT / "chat-option-tags.png"))
        btn = page.locator("[data-testid=project-chat-output-agent-comm-0002]")
        print("second output tag", btn.evaluate("el => el.tagName"))
        btn.click()
        page.wait_for_timeout(400)
        print("url after click", page.url)
        focused = page.locator("[data-comm-id=comm-0001]")
        print("first has ring", "ring-2" in (focused.get_attribute("class") or ""))
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        print("mobile first", page.locator("[data-testid=project-chat-header-comm-0001]").inner_text().replace("\n", " | "))
        page.screenshot(path=str(OUT / "chat-header-mobile.png"))
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
