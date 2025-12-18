from utils.regex_helper import safe_search
import re

def parse(text):
    text = text.upper()

    # Card No: 4695 25XX XXXX 3458
    card_last_4 = safe_search(
        r"CARD NO\s*:\s*\d{4}\s+\w{2}XX\s+XXXX\s+(\d{4})",
        text
    )

    # Statement Date (used as billing reference)
    billing_cycle = safe_search(
        r"STATEMENT DATE\s*[:\-]?\s*(\d{2}/\d{2}/\d{4})",
        text
    )

    # Locate the summary header once
    summary_block = re.search(
        r"PAYMENT DUE DATE\s+TOTAL DUES\s+MINIMUM AMOUNT DUE([\s\S]{0,200})",
        text
    )

    payment_due_date = None
    total_amount_due = None

    if summary_block:
        block = summary_block.group(1)

        # First date after header → Payment Due Date
        date_match = re.search(r"\d{2}/\d{2}/\d{4}", block)
        if date_match:
            payment_due_date = date_match.group(0)

        # First amount after header → Total Dues
        amount_match = re.search(r"([\d,]+\.\d{2})", block)
        if amount_match:
            total_amount_due = amount_match.group(1)

    return {
        "issuer": "HDFC",
        "card_last_4": card_last_4,
        "billing_cycle": billing_cycle,
        "payment_due_date": payment_due_date,
        "total_amount_due": total_amount_due
    }
