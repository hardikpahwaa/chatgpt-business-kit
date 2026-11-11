# ChatGPT Business Kit

**Get your business set up properly inside ChatGPT.** OpenAI just launched *Businesses in ChatGPT* (Business Hub, Insights and Business Agents). This Claude skill walks you through claiming and verifying your business, writes a profile that matches your website, checks that ChatGPT can actually read your site, builds a rule-safe Business Agent, and tracks your Insights every month.

Give it your website and ask *"Set my business up on ChatGPT."*

## What you get

| Mode | What it does |
|---|---|
| 1. Eligibility + plan | Which parts you get for your country and business type, and your first 3 actions |
| 2. Claim + verify | Step-by-step claim, the right ownership method for you, and a prep list so identity verification doesn't fail |
| 3. Profile writer | Ready-to-paste category, description and policies from your real website, plus a check for anything that contradicts your site |
| 4. Crawler check | Is ChatGPT's search bot allowed or blocked by robots.txt or your firewall? Exact lines to fix it |
| 5. Get recommended | 10 buyer questions to test in ChatGPT, who gets named instead of you, and the pages you're missing, ranked by evidence |
| 6. Business Agent builder | Instructions, a fact sheet, 15 test questions and a check against OpenAI's agent rules (US online businesses) |
| 7. Product feed check | Your CSV against the 9 required fields and value rules (stores) |
| 8. Insights tracker | What mentions, clicks and topics really mean, and a monthly tracker |

Or ask for the full **Launch Plan**: all of the above on one page.

Every fact is checked against OpenAI's own help pages, terms and policies (12 Nov 2026) and labelled when it comes from a blog or a single user report. It never promises ChatGPT will recommend you, and it warns you about the irreversible parts (published profiles can't be deleted) before you click.

## Install

**Claude Code**
```
/plugin marketplace add hardikpahwaa/chatgpt-business-kit
/plugin install chatgpt-business-kit@chatgpt-business-kit
```

**Claude.ai / Claude desktop app**
1. Download `chatgpt-business-kit.zip` from the [latest release](https://github.com/hardikpahwaa/chatgpt-business-kit/releases/latest)
2. Go to **Settings → Capabilities → Skills** and upload the zip

**Manual (Claude Code)**
```
git clone https://github.com/hardikpahwaa/chatgpt-business-kit
cp -R chatgpt-business-kit/skills/chatgpt-business-kit ~/.claude/skills/
```

## Use it

> Here's my site: https://example.com. Set my business up on ChatGPT.

> My Persona verification failed. What did I get wrong?

> Write my ChatGPT business profile and check it against my website.

> Is ChatGPT allowed to crawl my site?

> Build my ChatGPT Business Agent and test it.

Works best when Claude can browse the web and run code (for `check_site.py` and `check_feed.py`). Without that, it works from what you paste in.

## What's inside

```
skills/chatgpt-business-kit/
├── SKILL.md                          # the 8 modes and the Launch Plan
├── references/
│   ├── eligibility-and-claim.md      # who gets what, claim flow, 4 ownership methods
│   ├── persona-and-profile.md        # verification prep, profile template, consistency check
│   ├── crawlers-and-visibility.md    # OpenAI's bots, robots.txt lines, what helps you get recommended
│   ├── business-agent.md             # instructions template, 15 tests, policy lint
│   ├── product-feed.md               # feed spec for stores
│   ├── insights.md                   # metric definitions + monthly routine
│   ├── terms-and-gotchas.md          # the terms to read before you click, 14 gotchas
│   └── sources.md                    # every source, dated
├── scripts/
│   ├── check_site.py                 # robots.txt + firewall check for OpenAI's bots
│   └── check_feed.py                 # product feed CSV validator
└── templates/
    └── insights-tracker.csv          # monthly tracker
```

Want a deeper audit for every AI agent (Claude, Perplexity, browser agents, connectors)? See the companion skill [agent-ready-audit](https://github.com/hardikpahwaa/agent-ready-audit).

## Credits

Written by **Hardik Pahwa** ([@hardikpahwa.ai](https://www.instagram.com/hardikpahwa.ai/)). Built from OpenAI's help center, terms and policies, plus reporting by Digiday, PPC Land, Search Engine Roundtable, Ahrefs and hands-on guides. Full list in [sources.md](skills/chatgpt-business-kit/references/sources.md). Not affiliated with or endorsed by OpenAI. Not legal advice.

## License

MIT. See [LICENSE](LICENSE).
