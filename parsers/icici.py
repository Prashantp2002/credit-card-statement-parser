from utils.regex_helper import safe_search
import re

def parse(text):
    text = text.upper()

    # 1️⃣ Try extracting statement date using label
    statement_date = safe_search(
        r"STATEMENT DATE[\s:]*([0-9]{2}/[0-9]{2}/[0-9]{4})",
        text
    )

    # 2️⃣ Fallback: first date found in document
    if not statement_date:
        dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
        statement_date = dates[0] if dates else None

    return {
        "issuer": "ICICI",

        "card_last_4": safe_search(
            r"CARD NUMBER\s*:\s*\d{4}\s+XXXX\s+XXXX\s+(\d{4})",
            text
        ),

        # Billing cycle is derived from statement date (ICICI limitation)
        "billing_cycle": statement_date,

        "payment_due_date": safe_search(
            r"DUE DATE[\s:]*([0-9]{2}/[0-9]{2}/[0-9]{4})",
            text
        ),

        "total_amount_due": safe_search(
            r"YOUR TOTAL AMOUNT DUE[\s\S]{0,80}?([0-9,]+\.\d{2})",
            text
        )
    }
