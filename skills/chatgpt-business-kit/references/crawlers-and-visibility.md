# Can ChatGPT read you, and what helps you get recommended

## What OpenAI officially says
- Claiming "doesn't guarantee increased visibility or give you direct control over ChatGPT's independent recommendations." Advertising doesn't influence ChatGPT's answers.
- Clearer, accurate information "could help ChatGPT surface a business in more relevant conversations" (OpenAI VP, to Digiday).
- To be eligible for ChatGPT search answers: **allow OAI-SearchBot** in robots.txt **and** make sure your host/CDN allows OpenAI's published search-bot IP ranges.
- ChatGPT search sends rewritten queries to third-party search providers; OpenAI names **Microsoft** (Bing) and Shopify. So being indexed in Bing matters; how much is unpublished.
- Shopping results use structured product data (price, description), third-party content and review summaries; merchant ranking considers availability, price, quality and whether you're the maker/primary seller.

## OpenAI's crawlers
| Bot | What it does | If you block it |
|---|---|---|
| **OAI-SearchBot** | Finds pages for ChatGPT search answers | You won't be shown in ChatGPT search answers (only as plain navigational links). Takes ~24 h to apply. |
| **GPTBot** | Collects data for training models | Your content isn't used for training. Search is unaffected. **But** if you upload a product feed, OpenAI's terms ask you to allow its crawlers and not reserve data-mining opt-outs. Check with a lawyer if it matters to you. |
| **ChatGPT-User** | Visits a page when a user asks ChatGPT to | robots.txt may not apply; not used to decide search inclusion |
| **OAI-AdsBot** | Checks ad landing pages | Only visits pages you submit as ads |

IP ranges: https://openai.com/searchbot.json · https://openai.com/gptbot.json · https://openai.com/chatgpt-user.json

## Lines to paste into robots.txt
Allow search (recommended for anyone who wants to be found):
```
User-agent: OAI-SearchBot
Allow: /
```
Optional, only if you don't want your content used for training (and you don't upload a product feed):
```
User-agent: GPTBot
Disallow: /
```
Keep a `Sitemap: https://yoursite.com/sitemap.xml` line. OpenAI publishes no sitemap guidance, but it helps Bing.

## Firewall / CDN check
Cloudflare and other CDNs can block AI bots even when robots.txt allows them (Cloudflare: Security → Bots / "Block AI bots"; WAF rules). Make sure OAI-SearchBot isn't challenged or blocked, or allowlist OpenAI's IP ranges. Insights shows a "Website access" panel (one dashboard showed "Access confirmed"); OpenAI hasn't documented it.

## The mention rule changes your strategy
For online businesses, Insights only counts a **mention when ChatGPT cites your website**. Your brand name in an answer doesn't count. So the answers buyers want have to live on **your pages**.

## Visibility fixes, by evidence strength
**Strong (official):**
1. Allow OAI-SearchBot + OpenAI IPs at the CDN.
2. Claim, verify and keep the profile accurate and consistent with the site.
3. Stores: connect an accurate product feed (or Shopify).
**Medium (consistent across sources):**
4. Be indexed in Bing: Bing Webmaster Tools, sitemap submitted, IndexNow if your platform supports it. Bing Webmaster Tools also reports AI-search queries.
5. Be present where ChatGPT already cites: in Ahrefs' Nov 2026 US data the top cited domains were Wikipedia, Reddit, Consumer Reports, Walmart, then PubMed, FDA, YouTube, Home Depot, with BBB, Trustpilot, Tripadvisor and Angi in the top 30. Accurate listings and genuine reviews on the directories for your category.
6. Consistent name/address/phone across Google Business Profile, Bing Places, Apple Business Connect, Yelp.
**Weak (practitioner advice, no OpenAI statement):**
7. A page per buyer question: pricing in plain text, comparisons ("X vs Y"), "who it's for", FAQs; first sentence under each heading answers the question directly; specific numbers and names; visible last-updated dates; a named author.
8. Organization / Product / FAQ schema markup.
9. llms.txt (no evidence it matters for ChatGPT; don't prioritise).

## Buyer-prompt test (monthly)
Write 10 prompts real customers ask: "best [category] for [audience] in [city]", "[brand] vs [competitor]", "is [brand] worth it", "[brand] pricing", "alternatives to [competitor]", "[problem] solution for [audience]". Run them in a logged-out or fresh ChatGPT chat with search on. Record: are you named, is your site cited, who is named instead, which sites are cited, anything wrong about you. Fix wrong facts at the source (your site, then directories).
