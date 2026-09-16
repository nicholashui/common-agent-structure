from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"
OUT = Path("logs")


def node_xy(page):
    return page.evaluate(
        """() => [...document.querySelectorAll('.react-flow__node')].map((el) => {
          const box = el.getBoundingClientRect();
          return {
            id: el.getAttribute('data-id'),
            x: Math.round(box.x),
            y: Math.round(box.y),
            w: Math.round(box.width),
            h: Math.round(box.height),
          };
        })"""
    )


def overlap(nodes, gap=8):
    for i, left in enumerate(nodes):
        for right in nodes[i + 1 :]:
            if (
                left["x"] < right["x"] + right["w"] + gap
                and left["x"] + left["w"] + gap > right["x"]
                and left["y"] < right["y"] + right["h"] + gap
                and left["y"] + left["h"] + gap > right["y"]
            ):
                return True
    return False


def main() -> None:
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(25000)

        page.goto(f"{BASE}/projects/european-handsome/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-canvas]", timeout=20000)
        page.wait_for_timeout(1800)
        initial = node_xy(page)
        print("desktop_nodes", len(initial))
        print("desktop_overlap", overlap(initial))
        xs = sorted({row["x"] for row in initial})
        ys = sorted({row["y"] for row in initial})
        print("desktop_unique_x", len(xs), "unique_y", len(ys))

        page.locator("[data-testid=project-auto-layout-toggle]").click()
        page.wait_for_selector("[data-testid=project-auto-layout-menu]", timeout=5000)
        first = page.locator("[data-testid=project-auto-layout-menu] [role=menuitem]").first
        print("menu_first", first.get_attribute("data-testid"), first.get_attribute("data-default"))
        print("force_default", page.locator('[data-testid=project-auto-layout-force][data-default=true]').count())
        page.screenshot(path=str(OUT / "force-default-desktop.png"))

        page.locator("[data-testid=project-auto-layout-layered-lr]").click()
        page.wait_for_timeout(800)
        layered = node_xy(page)
        print("layered_changed", layered != initial)

        page.locator("[data-testid=project-auto-layout-toggle]").click()
        page.locator("[data-testid=project-auto-layout-force]").click()
        page.wait_for_timeout(800)
        force = node_xy(page)
        print("force_changed_from_layered", force != layered)
        print("force_overlap", overlap(force))

        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat]", timeout=20000)
        print("chat_ok", page.locator("[data-testid=project-chat]").count())

        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-canvas]", timeout=20000)
        page.wait_for_timeout(1600)
        print("asain_nodes", len(node_xy(page)))
        print("asain_overlap", overlap(node_xy(page)))

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-auto-layout]", timeout=20000)
        page.wait_for_timeout(1200)
        page.locator("[data-testid=project-auto-layout-toggle]").click()
        print("mobile_menu", page.locator("[data-testid=project-auto-layout-menu]").count())
        print("mobile_force_first", page.locator("[data-testid=project-auto-layout-menu] [role=menuitem]").first.get_attribute("data-testid"))
        page.screenshot(path=str(OUT / "force-default-mobile.png"))
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
