from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=True, channel="msedge")
    except Exception:
        browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1400, "height": 900})
    page.set_default_timeout(25000)
    page.goto(f"{BASE}/workflow", wait_until="domcontentloaded")
    page.wait_for_selector("[data-testid=agent-workflow]")
    page.wait_for_timeout(900)
    href = page.evaluate(
        """() => {
          const obj = document.querySelector("object[type='image/svg+xml']");
          const link = obj && obj.contentDocument && obj.contentDocument.querySelector("a.agent-link");
          return link ? link.getAttribute("href") : null;
        }"""
    )
    print("href", href)
    page.evaluate(
        """() => {
          const obj = document.querySelector("object[type='image/svg+xml']");
          const link = obj.contentDocument.querySelector("a.agent-link");
          link.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, view: window }));
        }"""
    )
    page.wait_for_timeout(1000)
    print("url", page.url)
    browser.close()
