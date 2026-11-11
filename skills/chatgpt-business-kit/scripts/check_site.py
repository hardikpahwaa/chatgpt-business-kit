#!/usr/bin/env python3
"""Can ChatGPT read this site? Checks robots.txt rules for OpenAI's bots and whether the
homepage answers a request sent with OAI-SearchBot's user agent.

Usage: python3 check_site.py https://example.com
Standard library only. A 403/429/challenge for the bot UA but not for a browser UA usually
means a firewall/CDN rule (e.g. Cloudflare "Block AI bots"). Note: real OAI-SearchBot traffic
comes from OpenAI's IP ranges (openai.com/searchbot.json); a CDN may treat this test differently.
"""
import sys, urllib.request, urllib.error, urllib.robotparser
from urllib.parse import urlparse

BOTS = ["OAI-SearchBot", "GPTBot", "ChatGPT-User", "Bingbot"]
UA = {
    "browser": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36",
    "OAI-SearchBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot",
}


def fetch(url, ua):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read(200000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return None, str(e)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    site = sys.argv[1].rstrip("/")
    if not site.startswith("http"):
        site = "https://" + site
    root = f"{urlparse(site).scheme}://{urlparse(site).netloc}"

    code, robots = fetch(root + "/robots.txt", UA["browser"])
    print(f"robots.txt: HTTP {code}")
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(robots.splitlines() if code == 200 else [])
    for bot in BOTS:
        ok = rp.can_fetch(bot, root + "/")
        note = {"OAI-SearchBot": "needed to appear in ChatGPT search answers",
                "GPTBot": "training only; your choice (see trade-off)",
                "ChatGPT-User": "user-triggered visits; robots.txt may not apply",
                "Bingbot": "ChatGPT search uses Microsoft as a provider"}[bot]
        print(f"  {bot:14} {'ALLOWED' if ok else 'BLOCKED'}   ({note})")
    sitemaps = [l.split(":", 1)[1].strip() for l in robots.splitlines() if l.lower().startswith("sitemap:")]
    print("  Sitemap line:", ", ".join(sitemaps) if sitemaps else "none (add one)")

    b, _ = fetch(root + "/", UA["browser"])
    s, body = fetch(root + "/", UA["OAI-SearchBot"])
    print(f"homepage: browser HTTP {b} | OAI-SearchBot UA HTTP {s}")
    challenge = any(k in body.lower() for k in ("cf-chl", "challenge-platform", "attention required", "just a moment"))
    if s != 200 or challenge:
        print("  WARNING: the bot request was blocked or challenged. Check your firewall/CDN bot settings "
              "and allowlist OpenAI's IP ranges (openai.com/searchbot.json).")
    elif b == 200:
        print("  OK: the homepage answers the OAI-SearchBot user agent.")

    if not rp.can_fetch("OAI-SearchBot", root + "/"):
        print("\nAdd to robots.txt to be eligible for ChatGPT search answers:\n  User-agent: OAI-SearchBot\n  Allow: /")


if __name__ == "__main__":
    main()
