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
        page.goto(f"{BASE}/projects/european-handsome/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-auto-layout]", timeout=20000)
        page.wait_for_timeout(1200)
        before = page.evaluate(
            """() => [...document.querySelectorAll('.react-flow__node')].map((el) => {
              const box = el.getBoundingClientRect();
              return `${el.getAttribute('data-id')}:${Math.round(box.x)}:${Math.round(box.y)}`;
            }).join('|')"""
        )
        page.locator("[data-testid=project-auto-layout-toggle]").click()
        page.wait_for_selector("[data-testid=project-auto-layout-menu]", timeout=5000)
        print("menu_open", page.locator("[data-testid=project-auto-layout-menu]").count())
        print("has_lr", page.locator("[data-testid=project-auto-layout-layered-lr]").count())
        print("has_tb", page.locator("[data-testid=project-auto-layout-layered-tb]").count())
        print("has_grid", page.locator("[data-testid=project-auto-layout-grid]").count())
        print("has_radial", page.locator("[data-testid=project-auto-layout-radial]").count())
        print("has_force", page.locator("[data-testid=project-auto-layout-force]").count())
        page.locator("[data-testid=project-auto-layout-grid]").click()
        page.wait_for_timeout(800)
        after_grid = page.evaluate(
            """() => [...document.querySelectorAll('.react-flow__node')].map((el) => {
              const box = el.getBoundingClientRect();
              return `${el.getAttribute('data-id')}:${Math.round(box.x)}:${Math.round(box.y)}`;
            }).join('|')"""
        )
        print("grid_changed", after_grid != before)
        page.locator("[data-testid=project-auto-layout-toggle]").click()
        page.locator("[data-testid=project-auto-layout-layered-tb]").click()
        page.wait_for_timeout(800)
        after_tb = page.evaluate(
            """() => [...document.querySelectorAll('.react-flow__node')].map((el) => {
              const box = el.getBoundingClientRect();
              return `${el.getAttribute('data-id')}:${Math.round(box.x)}:${Math.round(box.y)}`;
            }).join('|')"""
        )
        print("tb_changed", after_tb != after_grid)
        page.screenshot(path="logs/auto-layout-menu-desktop.png")
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-auto-layout]", timeout=20000)
        page.wait_for_timeout(800)
        page.locator("[data-testid=project-auto-layout-toggle]").click()
        print("mobile_menu", page.locator("[data-testid=project-auto-layout-menu]").count())
        page.screenshot(path="logs/auto-layout-menu-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
