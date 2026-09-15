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
        page.wait_for_selector("[data-testid=project-canvas]", timeout=20000)
        page.wait_for_timeout(1800)
        edges = page.locator(".react-flow__edge").count()
        print("project_edges", edges)
        overlap = page.evaluate(
            """() => {
              const nodes = [...document.querySelectorAll('.react-flow__node')];
              const boxes = nodes.map((el) => el.getBoundingClientRect());
              for (let i = 0; i < boxes.length; i++) {
                for (let j = i + 1; j < boxes.length; j++) {
                  const a = boxes[i], b = boxes[j];
                  if (a.left < b.right - 8 && a.right > b.left + 8 && a.top < b.bottom - 8 && a.bottom > b.top + 8) {
                    return true;
                  }
                }
              }
              return false;
            }"""
        )
        print("project_overlap", overlap)
        page.screenshot(path="logs/project-workflow-edges-desktop.png")

        page.goto(f"{BASE}/workflow/sub", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=sub-workflow-select]", timeout=20000)
        page.select_option("[data-testid=sub-workflow-select]", "video.template.b")
        page.wait_for_timeout(1500)
        clicked = page.evaluate(
            """() => {
              const host = document.querySelector('object');
              const doc = host && host.contentDocument;
              if (!doc) return false;
              const link = doc.querySelector('a.agent-link[href*="video.director"]') || doc.querySelector('a.agent-link');
              if (!link) return false;
              link.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: doc.defaultView }));
              return link.getAttribute('href');
            }"""
        )
        print("sub_click_href", clicked)
        page.wait_for_timeout(800)
        print("sub_url", page.url)

        page.goto(f"{BASE}/org-chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=org-chart]", timeout=20000)
        page.wait_for_timeout(1200)
        agent = page.locator(".react-flow__node").filter(has_text="video.director")
        print("org_director", agent.count())
        if agent.count():
            agent.first.click()
            page.wait_for_timeout(800)
        print("org_url", page.url)
        page.screenshot(path="logs/org-chat-click-desktop.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
