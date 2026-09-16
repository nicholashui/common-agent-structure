"""Live UI audit: routes, console, a11y, overflow. Prints compact findings."""

from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"
OUT = "logs"
ROUTES = [
    "/",
    "/projects",
    "/projects/new",
    "/projects/asain-beauty/start",
    "/projects/asain-beauty/workflow",
    "/projects/asain-beauty/chat",
    "/workflow",
    "/workflow/sub",
    "/org-chat",
    "/agents",
    "/agents/video.promptengineer",
    "/agents/video.promptengineer/chat",
    "/agents/video.promptengineer/files",
    "/agents/video.promptengineer/structure",
    "/settings",
    "/help",
]


def audit_page(page, route, width, height):
    errors = []
    page.on("pageerror", lambda err: errors.append(f"pageerror:{err}"))
    page.on("console", lambda msg: errors.append(f"console:{msg.type}:{msg.text}") if msg.type in {"error", "warning"} else None)
    page.set_viewport_size({"width": width, "height": height})
    resp = page.goto(f"{BASE}{route}", wait_until="domcontentloaded")
    page.wait_for_timeout(1200)
    status = resp.status if resp else 0
    overflow = page.evaluate(
        """() => {
          const doc = document.documentElement;
          return { scrollWidth: doc.scrollWidth, clientWidth: doc.clientWidth, overflow: doc.scrollWidth > doc.clientWidth + 8 };
        }"""
    )
    a11y = page.evaluate(
        """() => {
          const buttons = [...document.querySelectorAll('button, a, summary')];
          const unlabeled = buttons.filter((el) => {
            const text = (el.innerText || '').trim();
            const aria = el.getAttribute('aria-label') || el.getAttribute('title') || '';
            return !text && !aria;
          }).map((el) => el.outerHTML.slice(0, 120));
          const images = [...document.querySelectorAll('img')].filter((img) => !img.getAttribute('alt')).length;
          const inputs = [...document.querySelectorAll('input, select, textarea')].filter((el) => {
            const id = el.getAttribute('id');
            const aria = el.getAttribute('aria-label') || el.getAttribute('aria-labelledby');
            const label = id && document.querySelector(`label[for="${id}"]`);
            const wrap = el.closest('label');
            return !aria && !label && !wrap;
          }).map((el) => (el.getAttribute('data-testid') || el.getAttribute('name') || el.tagName).slice(0, 80));
          return { unlabeled: unlabeled.slice(0, 6), unlabeledCount: unlabeled.length, unlabeledImages: images, unlabeledInputs: inputs.slice(0, 8) };
        }"""
    )
    title = page.locator("h1, h2").first.inner_text() if page.locator("h1, h2").count() else ""
    slug = route.strip("/").replace("/", "_") or "home"
    page.screenshot(path=f"{OUT}/ux-{width}-{slug[:40]}.png", full_page=False)
    cons = [e for e in errors if "Download the React DevTools" not in e and "favicon" not in e]
    print(f"ROUTE {width}x{height} {route} status={status} overflow={overflow['overflow']} sw={overflow['scrollWidth']} title={title!r}")
    if a11y["unlabeledCount"] or a11y["unlabeledImages"] or a11y["unlabeledInputs"]:
        print("  a11y", a11y)
    if cons:
        print("  errors", cons[:8])


def main():
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(20000)
        for w, h in ((1400, 900), (390, 844)):
            for route in ROUTES:
                try:
                    audit_page(page, route, w, h)
                except Exception as exc:
                    print(f"ROUTE FAIL {w} {route} {exc}")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
