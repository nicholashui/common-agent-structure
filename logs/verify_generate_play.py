from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path("logs")
BASE = "http://127.0.0.1:15173"


def launch(p):
    for channel in ("msedge", "chrome"):
        try:
            browser = p.chromium.launch(headless=True, channel=channel)
            return browser, channel
        except Exception as exc:
            print("channel fail", channel, type(exc).__name__, str(exc)[:160])
    return p.chromium.launch(headless=True), "chromium"


def main() -> None:
    with sync_playwright() as p:
        browser, channel = launch(p)
        print("channel", channel)
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.set_default_timeout(20000)
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        tags = page.locator("[data-testid=project-generator-tags] button")
        print("tag count", tags.count())
        print("labels", tags.all_inner_texts())
        page.locator("[data-testid=project-chat-output]").scroll_into_view_if_needed()
        page.screenshot(path=str(OUT / "gen-tags.png"))
        cfg = page.locator("[data-testid=project-video-config] select")
        print("config selects", cfg.count(), [cfg.nth(i).input_value() for i in range(cfg.count())])
        video = page.locator("[data-testid=project-chat-video]")
        print("video count", video.count())
        last = page.locator("[data-testid=project-chat-log] li").last
        print("last", last.inner_text()[:500].replace("\n", " | "))
        if video.count():
            video.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            before = video.evaluate(
                """el => ({
                    src: el.currentSrc || el.src,
                    readyState: el.readyState,
                    networkState: el.networkState,
                    videoWidth: el.videoWidth,
                    duration: Number.isFinite(el.duration) ? el.duration : null,
                    paused: el.paused,
                    error: el.error && (el.error.message || String(el.error.code))
                })"""
            )
            print("before play", before)
            played = video.evaluate(
                """async el => {
                    try {
                        el.muted = true;
                        await el.play();
                        return {
                            ok: true,
                            paused: el.paused,
                            currentTime: el.currentTime,
                            videoWidth: el.videoWidth,
                            duration: Number.isFinite(el.duration) ? el.duration : null,
                            readyState: el.readyState
                        };
                    } catch (e) {
                        return {
                            ok: false,
                            name: e.name,
                            message: String(e.message || e),
                            paused: el.paused,
                            videoWidth: el.videoWidth,
                            networkState: el.networkState,
                            readyState: el.readyState
                        };
                    }
                }"""
            )
            print("play", played)
            page.screenshot(path=str(OUT / "gen-video-embed.png"))
        page.goto(f"{BASE}/projects/asain-beauty/flow", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        print("flow title", page.title(), "nodes", page.locator(".react-flow__node").count())
        page.screenshot(path=str(OUT / "gen-flow-regress.png"))
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(f"{BASE}/projects/asain-beauty/chat", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        page.locator("[data-testid=project-chat-output]").scroll_into_view_if_needed()
        print("mobile tags", page.locator("[data-testid=project-generator-tags] button").count())
        page.screenshot(path=str(OUT / "gen-mobile.png"))
        if page.locator("[data-testid=project-chat-video]").count():
            page.locator("[data-testid=project-chat-video]").scroll_into_view_if_needed()
            page.screenshot(path=str(OUT / "gen-video-mobile.png"))
        browser.close()
    print("done")


if __name__ == "__main__":
    main()
