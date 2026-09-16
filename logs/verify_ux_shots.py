from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.set_default_timeout(20000)
        page.goto(f"{BASE}/", wait_until="domcontentloaded")
        page.wait_for_timeout(900)
        print("unlabeled_home", page.locator("a[href='/']:not([aria-label])").count())
        print("switcher_w", page.locator("#agent-switcher").evaluate("el => Math.round(el.getBoundingClientRect().width)"))
        page.screenshot(path="logs/ux-after-home-mobile.png")
        page.goto(f"{BASE}/agents/video.promptengineer/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(800)
        page.screenshot(path="logs/ux-after-chat-mobile.png")
        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        page.screenshot(path="logs/ux-after-workflow-mobile.png")
        page.set_viewport_size({"width": 1400, "height": 900})
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        page.screenshot(path="logs/ux-after-pchat-desktop.png")
        page.goto(f"{BASE}/", wait_until="domcontentloaded")
        page.wait_for_timeout(800)
        page.screenshot(path="logs/ux-after-home-desktop.png")
        browser.close()
    print("ok")


if __name__ == "__main__":
    main()
