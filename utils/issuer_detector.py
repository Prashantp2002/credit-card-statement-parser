def detect_issuer(text):
    text = text.upper()

    if "HDFC" in text:
        return "HDFC"
    elif "ICICI" in text:
        return "ICICI"
    elif "SBI" in text:
        return "SBI"
    elif "AXIS" in text:
        return "Axis"
    elif "CITIBANK" in text or "CITI" in text:
        return "Citibank"
    elif "SAMPLE CREDIT CARD STATEMENT" in text:
        return "GENERIC"
    return "Unknown"
