from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"
ROLES = [
    "video.promptengineer",
    "video.director",
    "video.cinematographer",
    "video.mua_makeup",
    "video.continuity",
]


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(25000)
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat-log]", timeout=20000)
        page.wait_for_timeout(800)
        headers = page.locator("[data-testid^=project-chat-header-]").all_text_contents()
        print("n headers", len(headers))
        human_to = [row for row in headers if row.startswith("Human →")]
        print("human headers")
        for row in human_to:
            print(" ", row.split("|")[0].strip())
        joined = "\n".join(headers)
        for role in ROLES:
            print(f"has Human → {role}", f"Human → {role}" in joined)
        print("has cameraoperator human", "Human → video.cameraoperator" in joined)
        print("has critic human", "Human → video.critic" in joined)
        print("has intent", "intent-analysis-agent" in joined)
        print("has creative", "creative-agent" in joined)
        status = page.locator("[data-testid=project-autopilot-status]")
        print("autopilot", status.count(), status.inner_text() if status.count() else "")
        print("open asks", page.locator("[data-testid=project-human-asks]").count())
        page.screenshot(path="logs/autopilot-chat-desktop.png")
        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        print("intent node", page.locator("[data-testid=project-agent-node]").count())
        labels = page.locator(".casops-node").all_text_contents()
        print("has intent node text", any("intent" in t.lower() for t in labels))
        print("has creative node text", any("creative" in t.lower() for t in labels))
        page.screenshot(path="logs/autopilot-workflow-desktop.png")
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat-log]", timeout=20000)
        page.wait_for_timeout(600)
        page.screenshot(path="logs/autopilot-chat-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
