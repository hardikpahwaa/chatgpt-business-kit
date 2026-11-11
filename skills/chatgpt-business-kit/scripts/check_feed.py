#!/usr/bin/env python3
"""Check a product feed CSV against OpenAI's product feed spec (required fields + value rules).

Usage: python3 check_feed.py feed.csv
Standard library only. Prints a summary and the first problems per rule. Spec:
https://developers.openai.com/commerce/specs/file-upload/products (checked 12 Nov 2026).
"""
import csv, re, sys
from collections import defaultdict

REQUIRED = ["item_id", "title", "description", "url", "brand", "seller_name", "image_url", "availability", "price"]
AVAIL = {"in_stock", "out_of_stock", "pre_order", "backorder", "unknown"}
PLACEHOLDER = {"n/a", "na", "null", "none", "tbd", "-", "undefined"}
PRICE = re.compile(r"^\d+(\.\d{1,2})?\s+[A-Z]{3}$")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    with open(sys.argv[1], newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("No rows found.")
    cols = rows[0].keys()
    missing_cols = [c for c in REQUIRED if c not in cols]
    problems, ids = defaultdict(list), defaultdict(int)
    for i, r in enumerate(rows, start=2):
        for c in REQUIRED:
            v = (r.get(c) or "").strip()
            if c in cols and not v:
                problems[f"empty {c}"].append(i)
            elif v.lower() in PLACEHOLDER:
                problems[f"placeholder in {c}"].append(i)
        ids[r.get("item_id", "")] += 1
        if len(r.get("title") or "") > 150:
            problems["title > 150 chars"].append(i)
        if len(r.get("description") or "") > 5000:
            problems["description > 5000 chars"].append(i)
        for c in ("url", "image_url", "return_policy"):
            v = (r.get(c) or "").strip()
            if v and not v.startswith("https://"):
                problems[f"{c} not absolute https"].append(i)
        a = (r.get("availability") or "").strip()
        if a and a not in AVAIL:
            problems["availability not one of " + "/".join(sorted(AVAIL))].append(i)
        p = (r.get("price") or "").strip()
        if p and not PRICE.match(p):
            problems["price not like '79.99 USD'"].append(i)
        sp = (r.get("sale_price") or "").strip()
        if sp and p and PRICE.match(sp) and PRICE.match(p):
            if sp.split()[1] != p.split()[1] or float(sp.split()[0]) >= float(p.split()[0]):
                problems["sale_price not lower than price / different currency"].append(i)
    dupes = [k for k, n in ids.items() if n > 1 and k]
    print(f"Rows: {len(rows)} | columns: {len(cols)}")
    print("Missing required columns:", ", ".join(missing_cols) or "none")
    if dupes:
        print(f"Duplicate item_id ({len(dupes)}):", ", ".join(dupes[:10]))
    if not problems and not missing_cols and not dupes:
        print("OK: no problems found against the required-field rules.")
    for rule, lines in sorted(problems.items(), key=lambda x: -len(x[1])):
        print(f"- {rule}: {len(lines)} rows (e.g. lines {', '.join(map(str, lines[:8]))})")
    print("Reminder: products must also follow OpenAI's Commerce policies (restricted categories).")


if __name__ == "__main__":
    main()
