from utils.regex_helper import safe_search

def parse(text):
    return {
        "issuer": "Axis",

        "card_last_4": safe_search(
            r"XXXX\s*XXXX\s*XXXX\s*(\d{4})",
            text
        ),

        "billing_cycle": safe_search(
            r"STATEMENT PERIOD\s*[:\-]?\s*(\d{2}\s+\w+\s+\d{4}\s*-\s*\d{2}\s+\w+\s+\d{4})",
            text
        ),

        "payment_due_date": safe_search(
            r"PAYMENT DUE DATE\s*[:\-]?\s*(\d{2}\s+\w+\s+\d{4})",
            text
        ),

        "total_amount_due": safe_search(
            r"TOTAL DUE\s*(?:INR|₹)\s*([\d,]+\.\d{2})",
            text
        )
    }
