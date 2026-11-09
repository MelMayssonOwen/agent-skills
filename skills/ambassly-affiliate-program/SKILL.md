---
name: ambassly-affiliate-program
description: Run a Stripe-based affiliate program through the Ambassly MCP. Use when asked to create or update an affiliate program, invite or enrol affiliates, create per-content referral links, review referrals and commissions, or prepare a payout batch.
license: MIT
metadata:
  author: Ambassly
  version: "1.0.0"
  homepage: "https://ambassly.com/"
---

# Run an affiliate program with Ambassly

Help a merchant or creator operate an affiliate program in [Ambassly](https://go.ambassly.com/skill). Keys are scoped: a company key operates the merchant side, and an affiliate key operates that creator's own portal. Connection steps are in [references/setup.md](references/setup.md).

## Pick the right side first

- Merchant work uses company tools such as `list_programs`, `create_program`, `update_program`, `list_affiliates`, `list_referrals`, `list_commissions`, and `get_payout_batch`.
- Creator work uses `my_stats`, `my_links`, and `create_link`.
- If a tool is refused, the key is probably for the other side. Say so instead of retrying.

## Launch a program

1. Call `list_programs` first. Do not create a second program for a product that already has one.
2. Confirm the name, destination URL, commission rate, commission duration, and cookie window with the user.
3. Call `create_program` only after those exact values are confirmed.
4. Point the user to the tracking snippet and Stripe webhook docs. Attribution does not work until both are installed.
5. Use `create_affiliate_invite` when the affiliate should accept by email, or `create_affiliate` for direct enrolment.

## Review money carefully

Commission and payout actions move real money, so treat them as human decisions.

1. Call `list_pending_commissions` and show the affiliate, amount, and source referral.
2. Ask for an explicit decision on each commission, or on a clearly stated group.
3. Call `approve_commission` or `reject_commission` only for what the user named. A rejection needs a reason.
4. Call `get_payout_batch` to prepare a payout, and present it as a list to pay. It does not send money.

## Links and reporting

- Use `create_link` or `create_affiliate_link` for one link per video, post, or newsletter so that each piece of content can be measured.
- Use `get_program_stats`, `list_referrals`, and `list_commissions` for reporting. Report the numbers returned and do not estimate missing ones.

## Secrets

Keep API keys and Stripe signing secrets in the client's secret settings. Do not print them, commit them, or paste them into chat. Only call `add_stripe_webhook_secret` when the user has supplied the value through a secure route.
