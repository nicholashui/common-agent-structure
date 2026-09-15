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

        page.goto(f"{BASE}/projects/european-handsome/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat-output]", timeout=20000)
        page.wait_for_selector("[data-testid=project-compile-note]", timeout=20000)
        note = page.inner_text("[data-testid=project-compile-note]")
        print("compile_note", "compiled from canonical v2" in note)
        print("no_auto_eval", "eval PASS" not in page.inner_text("body").upper())
        print("engine", page.locator("[data-testid=project-engine]").count())
        print("mode", page.locator("[data-testid=project-video-config] select").count())
        print("chips", page.locator("[data-testid=project-disposition-chips] [data-disposition]").count())
        print("chip_exact", page.locator("[data-testid=project-disposition-chips] [data-disposition=exact]").count())
        print("chip_prompted", page.locator("[data-testid=project-disposition-chips] [data-disposition=prompted]").count())
        print("generators", page.locator("[data-testid=project-generator-tags] button").count())
        print("section_subject", page.locator("[data-testid='project-section-Subject']").count())
        print("owner_light", page.locator("[data-testid='project-section-owner-Light']").count())
        print("owner_subject", page.locator("[data-testid='project-section-owner-Subject']").count())
        print("dry_run_control", page.locator("text=Dry-run").count())
        page.screenshot(path="logs/p5-chat-compile-desktop.png")

        page.locator("[data-testid='project-section-owner-Light']").click()
        page.wait_for_timeout(500)
        print("after_owner_url", page.url)
        print("owner_hop_comm", "comm=" in page.url)

        page.locator("[data-testid=project-engine]").select_option("seedance")
        page.wait_for_timeout(800)
        print("seedance_warn", page.locator("[data-testid=project-critic-warnings]").count())
        print("seedance_unsupported", page.locator("[data-testid=project-disposition-chips] [data-disposition=unsupported]").count())

        page.locator("[data-testid=project-generator-grok-imagine]").click()
        page.wait_for_timeout(1200)
        body = page.inner_text("body")
        print("generate_click_dry_run", "Dry-run" in body)
        print("no_live_mp4_after_dry", page.locator("[data-testid=project-chat-video]").count())

        page.goto(f"{BASE}/projects/european-handsome/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-agent-node]", timeout=20000)
        page.wait_for_timeout(600)
        owned = page.locator("[data-testid^=project-owned-path-]").count()
        print("workflow_owned_paths", owned)
        print("workflow_chat_buttons", page.locator("[data-testid^=project-open-chat-]").count())
        page.screenshot(path="logs/p5-workflow-owned-desktop.png")

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-chat-output]", timeout=20000)
        page.wait_for_timeout(600)
        print("mobile_compile", "compiled from canonical v2" in page.inner_text("[data-testid=project-compile-note]"))
        print("mobile_engine", page.locator("[data-testid=project-engine]").count())
        print("mobile_owner", page.locator("[data-testid='project-section-owner-Subject']").count())
        page.screenshot(path="logs/p5-chat-compile-mobile.png")

        page.goto(f"{BASE}/projects/asain-beauty/workflow", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-agent-node]", timeout=20000)
        page.wait_for_timeout(500)
        print("mobile_owned", page.locator("[data-testid^=project-owned-path-]").count())
        page.screenshot(path="logs/p5-workflow-owned-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
