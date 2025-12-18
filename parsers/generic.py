from utils.regex_helper import safe_search

def parse(text):
    return {
        "issuer": "Generic / Sample Statement",

        "card_last_4": safe_search(
            r"ACCOUNT NUMBER:\s*.*(\d{4})", text
        ),

        "billing_cycle": safe_search(
            r"OPENING/CLOSING DATE\s*([\d/XX\s–-]+)", text
        ),

        "payment_due_date": safe_search(
            r"PAYMENT DUE DATE:\s*([\d/XX]+)", text
        ),

        "total_amount_due": safe_search(
            r"NEW BALANCE:\s*\$([\d,]+\.\d{2})", text
        )
    }
