from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:15173"
OUT = "logs"


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.set_default_timeout(25000)

        page.goto(f"{BASE}/", wait_until="domcontentloaded")
        page.wait_for_timeout(900)
        home = page.locator('a[aria-label="Agent Swarm"]').count()
        crumb = page.locator("[data-testid=page-location]").inner_text()
        print("mobile_home_aria", home, "crumb", crumb)
        print("mobile_home_as_of_dash", "as_of —" in page.locator("body").inner_text())
        page.screenshot(path=f"{OUT}/ux-after-home-mobile.png")

        page.goto(f"{BASE}/agents/video.promptengineer/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=agent-chat]", timeout=20000)
        page.wait_for_timeout(800)
        print("mobile_chat_crumb", page.locator("[data-testid=page-location]").inner_text())
        print("mobile_chat_empty", page.locator("[data-testid=chat-log]").inner_text()[:80].replace("\n", " "))
        print("mobile_home_unlabeled_link", page.locator('a[href="/"]:not([aria-label])').count())
        page.screenshot(path=f"{OUT}/ux-after-chat-mobile.png")

        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-flow]", timeout=20000)
        page.wait_for_timeout(1400)
        print("mobile_wf_crumb", page.locator("[data-testid=page-location]").inner_text())
        print("mobile_first_instruction", page.locator("[data-testid=project-first-instruction]").get_attribute("aria-label"))
        print("mobile_canvas_autolayout", page.locator("[data-testid=project-canvas-auto-layout]").count())
        print("mobile_header_autolayout", page.locator("[data-testid=project-auto-layout]").count())
        page.screenshot(path=f"{OUT}/ux-after-workflow-mobile.png")

        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat]", timeout=20000)
        page.wait_for_timeout(1600)
        print("mobile_pchat_crumb", page.locator("[data-testid=page-location]").inner_text())
        print("mobile_pchat_hops", page.locator("[data-testid=project-chat-log] li").count())
        print("mobile_pchat_loading_gone", page.locator("[data-testid=project-chat-loading]").count())
        page.screenshot(path=f"{OUT}/ux-after-pchat-mobile.png")

        page.goto(f"{BASE}/settings", wait_until="domcontentloaded")
        page.wait_for_timeout(600)
        print("settings_as_of_dash", "as_of —" in page.locator("main").inner_text())
        print("settings_known_ids_label", page.locator("textarea[aria-label='Known agent IDs']").count())
        page.screenshot(path=f"{OUT}/ux-after-settings-mobile.png")

        page.set_viewport_size({"width": 1400, "height": 900})
        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        print("desktop_canvas_autolayout", page.locator("[data-testid=project-canvas-auto-layout]").count())
        print("desktop_wf_crumb", page.locator("[data-testid=page-location]").inner_text())
        page.screenshot(path=f"{OUT}/ux-after-workflow-desktop.png")

        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        page.screenshot(path=f"{OUT}/ux-after-pchat-desktop.png")

        page.goto(f"{BASE}/", wait_until="domcontentloaded")
        page.wait_for_timeout(900)
        page.screenshot(path=f"{OUT}/ux-after-home-desktop.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
