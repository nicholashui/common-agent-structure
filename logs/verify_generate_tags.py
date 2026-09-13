from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path("logs")
BASE = "http://127.0.0.1:15173"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(20000)
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        tags = page.locator("[data-testid=project-generator-tags] button")
        print("tag count", tags.count(), "labels", tags.all_inner_texts())
        page.locator("[data-testid=project-chat-output]").scroll_into_view_if_needed()
        page.screenshot(path=str(OUT / "gen-tags.png"))
        dry = page.locator("#dry-run-toggle")
        if dry.count() and dry.is_checked():
            dry.uncheck()
            page.wait_for_timeout(200)
        print("dry-run", dry.is_checked() if dry.count() else "missing")
        page.locator("[data-testid=project-generator-kling]").click()
        page.wait_for_timeout(1500)
        last = page.locator("[data-testid=project-chat-log] li").last
        print("kling last", last.inner_text()[:240].replace("\n", " | "))
        page.screenshot(path=str(OUT / "gen-kling.png"))
        page.locator("[data-testid=project-video-config] select").nth(1).select_option("6")
        page.locator("[data-testid=project-video-config] select").nth(2).select_option("480p")
        print("config set 6s 480p")
        page.locator("[data-testid=project-generator-grok-imagine]").click()
        try:
            page.wait_for_selector("[data-testid=project-chat-video]", timeout=240000)
            print("video embedded")
            page.locator("[data-testid=project-chat-video]").scroll_into_view_if_needed()
            page.screenshot(path=str(OUT / "gen-video.png"))
            exists = Path("project/asain-beauty/output/asain-beauty.mp4").is_file()
            print("mp4 on disk", exists, Path("project/asain-beauty/output/asain-beauty.mp4").stat().st_size if exists else 0)
        except Exception as exc:
            print("generate wait failed", type(exc).__name__, str(exc)[:300])
            err = page.locator("[data-testid=project-chat-log] li").last.inner_text()
            print("last after generate", err[:400].replace("\n", " | "))
            banner = page.locator("body").inner_text()
            if "Dry-run" in banner:
                print("saw dry-run copy")
            page.screenshot(path=str(OUT / "gen-video-fail.png"))
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        page.locator("[data-testid=project-chat-output]").scroll_into_view_if_needed()
        print("mobile tags", page.locator("[data-testid=project-generator-tags] button").count())
        page.screenshot(path=str(OUT / "gen-mobile.png"))
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
