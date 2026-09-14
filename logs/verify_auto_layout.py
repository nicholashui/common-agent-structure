from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path("logs")
BASE = "http://127.0.0.1:15173"


def node_transform(page, testid: str) -> str:
    loc = page.locator(f"[data-testid={testid}]").first
    if not loc.count():
        return ""
    return loc.evaluate(
        """el => {
            const node = el.closest('.react-flow__node');
            return node ? node.style.transform : '';
        }"""
    )


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(25000)

        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        print("project header", page.locator("[data-testid=project-auto-layout]").count())
        print("project canvas", page.locator("[data-testid=project-canvas-auto-layout]").count())
        before = node_transform(page, "project-start-node")
        print("start before", before)
        page.locator("[data-testid=project-canvas-auto-layout]").click()
        page.wait_for_timeout(700)
        after = node_transform(page, "project-start-node")
        print("start after", after)
        page.screenshot(path=str(OUT / "auto-layout-project.png"))

        page.goto(f"{BASE}/org-chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        print("org header", page.locator("[data-testid=org-auto-layout]").count())
        print("org canvas", page.locator("[data-testid=org-canvas-auto-layout]").count())
        page.locator("[data-testid=org-canvas-auto-layout]").click()
        page.wait_for_timeout(700)
        page.screenshot(path=str(OUT / "auto-layout-org.png"))

        page.goto(f"{BASE}/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        print("main workflow", page.locator("[data-testid=workflow-auto-layout]").count())
        page.locator("[data-testid=workflow-auto-layout]").click()
        page.wait_for_timeout(400)
        page.screenshot(path=str(OUT / "auto-layout-main.png"))

        page.goto(f"{BASE}/workflow/sub", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        print("sub workflow", page.locator("[data-testid=sub-workflow-auto-layout]").count())
        page.locator("[data-testid=sub-workflow-auto-layout]").click()
        page.wait_for_timeout(400)
        page.screenshot(path=str(OUT / "auto-layout-sub.png"))

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        print("mobile header", page.locator("[data-testid=project-auto-layout]").count())
        page.screenshot(path=str(OUT / "auto-layout-project-mobile.png"))
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
