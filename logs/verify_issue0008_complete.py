from playwright.sync_api import sync_playwright
import json
import urllib.request

BASE = "http://127.0.0.1:15173"
API = "http://127.0.0.1:18080"


def get(path: str) -> dict:
    with urllib.request.urlopen(API + path, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> None:
    swarms = get("/api/v3/swarms")
    print("swarms", [row.get("swarm_id") for row in swarms.get("swarms") or []])
    one = get("/api/v3/swarms/video.asain-beauty")
    print("runner", one.get("runner"), "members", len(one.get("member_ids") or []))
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(25000)
        page.goto(f"{BASE}/?swarm=video.asain-beauty", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        print("fleet_swarm_filter", page.locator("[data-testid=fleet-swarm-filter]").count() > 0)
        count = page.locator("[data-testid=fleet-count]").inner_text()
        print("fleet_count", count)
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat-log]", timeout=20000)
        print("cycle_gate", page.locator("[data-testid=project-cycle-gate]").count() > 0)
        if page.locator("[data-testid=project-cycle-gate]").count():
            page.locator("[data-testid=project-cycle-continue]").click()
            page.wait_for_timeout(800)
            print("after_continue_asks", page.locator("[data-testid=project-human-asks]").count() > 0)
        browser.close()


if __name__ == "__main__":
    main()
