from utils.regex_helper import safe_search

def parse(text):
    return {
        "issuer": "SBI",

        "card_last_4": safe_search(
            r"CARD\s*NO.*?(\d{4})",
            text
        ),

        "billing_cycle": safe_search(
            r"STATEMENT PERIOD\s*(\d{2}\s+\w+\s+\d{4}\s*-\s*\d{2}\s+\w+\s+\d{4})",
            text
        ),

        "payment_due_date": safe_search(
            r"PAYMENT DUE DATE\s*(\d{2}\s+\w+\s+\d{4})",
            text
        ),

        "total_amount_due": safe_search(
            r"TOTAL AMOUNT DUE\s*(?:RS\.?|INR)\s*([\d,]+\.\d{2})",
            text
        )
    }
