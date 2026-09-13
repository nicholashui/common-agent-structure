from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path("logs")
BASE = "http://127.0.0.1:15173"


def doc_y(page, selector: str) -> float:
    loc = page.locator(selector).first
    loc.scroll_into_view_if_needed()
    page.wait_for_timeout(200)
    return loc.evaluate("el => el.getBoundingClientRect().top + window.scrollY")


def main() -> None:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True, channel="msedge")
        except Exception:
            browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(20000)
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        log_last = page.locator("[data-testid=project-chat-log] li").last
        print("conversation last", log_last.inner_text()[:180].replace("\n", " | "))
        clip_first = page.locator("[data-testid=project-chat-clips] li").first
        clip_last = page.locator("[data-testid=project-chat-clips] li").last
        print("clips count", page.locator("[data-testid=project-chat-clips] li").count())
        print("clip first", clip_first.inner_text()[:180].replace("\n", " | "))
        print("clip last", clip_last.inner_text()[:180].replace("\n", " | "))
        y_log = doc_y(page, "[data-testid=project-chat-log]")
        y_out = doc_y(page, "[data-testid=project-chat-output]")
        y_clips = doc_y(page, "[data-testid=project-chat-clips]")
        print("y log/output/clips", round(y_log), round(y_out), round(y_clips))
        print("order ok", y_log < y_out < y_clips)
        video = page.locator("[data-testid=project-chat-video]")
        print("video in clips", page.locator("[data-testid=project-chat-clips] [data-testid=project-chat-video]").count())
        print("video in log", page.locator("[data-testid=project-chat-log] [data-testid=project-chat-video]").count())
        if video.count():
            video.scroll_into_view_if_needed()
            played = video.evaluate(
                """async el => {
                    try {
                        el.muted = true;
                        await el.play();
                        return { ok: true, paused: el.paused, duration: el.duration, readyState: el.readyState };
                    } catch (e) {
                        return { ok: false, message: String(e.message || e) };
                    }
                }"""
            )
            print("play", played)
        page.locator("[data-testid=project-chat-output]").scroll_into_view_if_needed()
        page.screenshot(path=str(OUT / "seq-instruction.png"))
        page.locator("[data-testid=project-chat-clips]").scroll_into_view_if_needed()
        page.screenshot(path=str(OUT / "seq-clips.png"))
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        y_log_m = doc_y(page, "[data-testid=project-chat-log]")
        y_out_m = doc_y(page, "[data-testid=project-chat-output]")
        y_clips_m = doc_y(page, "[data-testid=project-chat-clips]")
        print("mobile y", round(y_log_m), round(y_out_m), round(y_clips_m), "ok", y_log_m < y_out_m < y_clips_m)
        page.locator("[data-testid=project-chat-clips]").scroll_into_view_if_needed()
        page.screenshot(path=str(OUT / "seq-clips-mobile.png"))
        page.goto(f"{BASE}/projects/asain-beauty", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        print("flow comms", page.locator("[data-testid=project-comms] article").count())
        page.screenshot(path=str(OUT / "seq-flow.png"))
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
