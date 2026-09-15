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
        page.wait_for_selector("[data-testid=project-sequence]", timeout=20000)
        page.locator("[data-testid=project-sequence]").scroll_into_view_if_needed()
        note = page.inner_text("[data-testid=project-sequence-note]")
        print("sequence_note_clip_unit", "generation unit: clip" in note)
        print("sequence_one_clip", "1 clip" in note)
        print("sequence_concat_post", "concat post" in note)
        print("no_fused_copy", "whole sequence" in note.lower())
        print("clip_button", page.locator("[data-testid^=project-sequence-clip-]").count())
        print("compile_note", "compiled from canonical v2" in page.inner_text("[data-testid=project-compile-note]"))
        print("generators", page.locator("[data-testid=project-generator-tags] button").count())
        print("hops", "44 hop" in page.inner_text("body"))
        page.screenshot(path="logs/p6-sequence-desktop.png")

        page.locator("[data-testid=project-generator-grok-imagine]").click()
        page.wait_for_timeout(1200)
        print("dry_run_after_click", "Dry-run" in page.inner_text("body"))

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_selector("[data-testid=project-sequence]", timeout=20000)
        page.locator("[data-testid=project-sequence]").scroll_into_view_if_needed()
        mobile_note = page.inner_text("[data-testid=project-sequence-note]")
        print("mobile_sequence", "generation unit: clip" in mobile_note)
        print("mobile_hops", "44 hop" in page.inner_text("body"))
        page.screenshot(path="logs/p6-sequence-mobile.png")
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
