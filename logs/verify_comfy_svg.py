from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path("logs")
BASE = "http://127.0.0.1:15173"


def inspect_object(page) -> dict:
    page.wait_for_selector("object[type='image/svg+xml']", timeout=20000)
    page.wait_for_timeout(900)
    return page.evaluate(
        """() => {
          const obj = document.querySelector("object[type='image/svg+xml']");
          if (!obj) return { loaded: false, reason: "no-object" };
          const doc = obj.contentDocument;
          if (!doc || !doc.documentElement) return { loaded: false, reason: "no-doc" };
          const html = doc.documentElement.innerHTML || "";
          return {
            loaded: true,
            comfy: doc.querySelectorAll(".comfy-node").length,
            start: doc.querySelectorAll('[data-node-kind="start"]').length,
            agent: doc.querySelectorAll('[data-node-kind="agent"]').length,
            human: doc.querySelectorAll('[data-node-kind="human"]').length,
            output: doc.querySelectorAll('[data-node-kind="output"]').length,
            sockets: doc.querySelectorAll("circle.socket").length,
            links: doc.querySelectorAll("a.agent-link").length,
            title: (doc.querySelector(".header-title") || {}).textContent || "",
            bpmTitle: html.includes("BPM Workflow"),
            visual: doc.documentElement.getAttribute("data-visual-system") || "",
          };
        }"""
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1400, "height": 900}, bypass_csp=True)
        page = context.new_page()
        page.set_default_timeout(25000)
        page.route("**/*.svg", lambda route: route.continue_(headers={**route.request.headers, "Cache-Control": "no-cache"}))

        page.goto(f"{BASE}/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=agent-workflow]", timeout=20000)
        main_info = inspect_object(page)
        print("main", main_info)
        print("main auto", page.locator("[data-testid=workflow-auto-layout]").count())
        page.screenshot(path=str(OUT / "comfy-main-desktop.png"), full_page=False)

        toggle = page.locator("[data-testid=theme-toggle]")
        if toggle.count():
            toggle.click()
            page.wait_for_timeout(400)
            page.screenshot(path=str(OUT / "comfy-main-light.png"))
            toggle.click()
            page.wait_for_timeout(300)

        page.goto(f"{BASE}/workflow/sub", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=agent-sub-workflow]", timeout=20000)
        sub_info = inspect_object(page)
        print("sub template", sub_info)
        print("sub auto", page.locator("[data-testid=sub-workflow-auto-layout]").count())
        page.screenshot(path=str(OUT / "comfy-sub-desktop.png"))

        select = page.locator("[data-testid=sub-workflow-select]")
        if select.count():
            select.select_option(label="Scale S4")
            page.wait_for_timeout(1200)
            scale_info = inspect_object(page)
            print("sub scale", scale_info)
            page.screenshot(path=str(OUT / "comfy-sub-scale.png"))

        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        print("project start", page.locator("[data-testid=project-start-node]").count())
        print("project agent", page.locator("[data-testid=project-agent-node]").count())
        page.screenshot(path=str(OUT / "comfy-project-desktop.png"))

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=agent-workflow]", timeout=20000)
        page.wait_for_timeout(800)
        page.screenshot(path=str(OUT / "comfy-main-mobile.png"))
        page.goto(f"{BASE}/workflow/sub", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=agent-sub-workflow]", timeout=20000)
        page.wait_for_timeout(800)
        page.screenshot(path=str(OUT / "comfy-sub-mobile.png"))
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
