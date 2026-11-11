# Product feed (stores)

## Ways to connect (Business Hub, after Persona)
- **Shopify:** products are already in ChatGPT shopping through Shopify Catalog; the ChatGPT app can also handle verification. It asks for broad permissions (customer names/emails/IPs/browsing, owner details, editing pixels/marketing events). Read them before installing; domain or email verification avoids the app.
- **CSV upload** following OpenAI's product feed spec.
- **Hosted URL** pointing to your feed file.
- Large merchants can apply for direct feeds at chatgpt.com/merchants (SFTP, full snapshot at least daily, parquet preferred).
Connecting a feed doesn't publish an agent or guarantee recommendations. It must follow OpenAI's Commerce policies.

## Required fields (one row per purchasable item/variant)
| Field | Rule |
|---|---|
| `item_id` | Unique, stable |
| `title` | Aim ≤150 characters, plain text |
| `description` | ≤5,000 characters, plain text |
| `url` | Absolute https product page |
| `brand` | |
| `seller_name` | |
| `image_url` | Absolute https, publicly accessible |
| `availability` | `in_stock`, `out_of_stock`, `pre_order`, `backorder` or `unknown` (empty rejects the row) |
| `price` | Number + currency, e.g. `79.99 USD` |

## Useful optional fields
`sale_price` (must be lower than price, same currency) · `group_id` + `listing_has_variations` + `variant_dict` for variants · `gtin` / `mpn` · `condition` · `product_category` · `shipping_price` (empty means unknown, not free) · `accepts_returns` · `return_deadline_in_days` · `return_policy` (URL) · `is_eligible_search` (default true).

## Value rules
UTF-8. No placeholder strings ("n/a", "null", "TBD"). Absolute HTTPS URLs. The shared market format currently covers US, CA and MX; standard uploads use US, so non-US feeds may not be supported yet (unconfirmed for Business Hub). Common ingestion failures: missing required fields, outdated field names, malformed values.

## Terms to know
If you provide a feed, OpenAI's terms ask you to let its crawlers and agents access your site and not to reserve text-and-data-mining opt-outs against OpenAI. If you block GPTBot, decide which matters more.
