# Eligibility and claim flow
Checked against OpenAI's help article "Setting up your business on ChatGPT" on 12 Nov 2026. Beta: re-check before quoting.

## Who gets what
| Business type | Claim existing listing | Add a new listing | Edit profile + Insights (after identity check) | Product feed | Business Agent |
|---|---|---|---|---|---|
| Online store, US | Yes | Yes (an add option may appear) | Yes | Yes | Yes, if the industry passes OpenAI's agent review |
| Online service (software, agency, course), US | Yes | Yes (may) | Yes | Only if selling products | Yes, if the industry passes review; rolling out by business type |
| Local shop / restaurant, US | Yes, existing US listing only | Not yet | Yes | Not stated | No (agents are for ecommerce + online services) |
| Local shop / restaurant, outside US | Not yet | No | n/a | n/a | No |
| Online business, outside US | Yes, where ChatGPT and the required verification are supported | May see add option | Yes | Feed spec assumes US market today (unconfirmed for Hub uploads) | No (US only, no date) |

- No ads account, no Enterprise plan and no paid ChatGPT plan needed. Claiming is free (for now).
- No public country list. OpenAI: availability "depends on the business's location and type".
- OpenAI may decline or defer categories with safety/integrity concerns. Feeds must follow OpenAI's Commerce policies, which ban e.g. alcohol >0.5% ABV, tobacco/vapes, many supplements, prescription drugs, CBD/THC, firearms, crypto/NFT sales, debt relief, gambling, adult products, follower/like services, lead lists, in-game currency.
- Verification of the business doesn't guarantee agent eligibility.
- Launch-week reports [anecdotal]: some claims went to a waitlist; "Service" showed "Coming soon" for one tester.
- Big brands / existing advertisers can claim through an OpenAI rep; "managed" brands have location profiles locked.

## Claim flow
1. **Sign in** to ChatGPT with an account the **company** controls (not a freelancer's or ex-employee's). The claiming account becomes the admin.
2. **Open Business Hub** (sidebar or chatgpt.com/business-hub) and **search the business name**. Watch for old addresses, duplicates and look-alikes in other cities. Got a claim invitation email? Open its link and sign in with that exact address; don't forward it.
   - "Contact support" on a listing = locked.
   - Not listed and online-only: an add / create option may appear (fields seen: contact phone + email, category, short description, delivery policy, return policy; saved as a draft).
3. **Select the listing** and confirm the managing account. Continuing accepts the Businesses in ChatGPT Terms (read `terms-and-gotchas.md` first).
4. **Prove ownership** with one of the methods offered (you may not see all four):
   | Method | How | Pick it when | Watch out |
   |---|---|---|---|
   | Business phone | SMS or automated call to the number **on the listing** | The listed number rings you | Tracking numbers / old lines can't receive it |
   | Business email | Code sent to the email **associated with the business** | You control that inbox | Same: it's the listed address, not yours |
   | Website domain | Add the TXT record exactly (type, host, value) to your DNS, then "Verify domain" | You (or your developer) can edit DNS | **Add the record and wait for it to propagate before clicking Verify**; one user hit "too many attempts" |
   | Shopify | Connect Shopify → approve permissions → log in to the store | Shopify store owners who accept the app's permissions | The app asks for broad customer-data permissions; launch reviews report verification loops |
5. **Wait for review.** OpenAI emails a decision or asks for more info. No published time: some were approved in minutes, others waitlisted. You can cancel while pending.
6. **Identity verification (Persona)** is next and separate. Until it's approved: no blue check, no edits, no feed, no Insights, no agent. See `persona-and-profile.md`.

## Team, agencies, disputes
- The admin can add teammates and give an agency access. Everyone uses their own ChatGPT account.
- Each brand is managed separately; claiming the main brand doesn't claim its locations.
- **Someone else claimed it:** profile → ••• → **Dispute ownership** → verify with Persona. Disputing doesn't change visibility.
- Tell OpenAI if your authority changes (owner sells, staff leaves).
- After approval you may see an upsell for "ChatGPT Business" (a different, paid subscription) and, for some, ads credit. Neither is needed.
