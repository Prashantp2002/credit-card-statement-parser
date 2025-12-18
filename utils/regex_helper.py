import re

def safe_search(pattern, text, flags=re.I):
    match = re.search(pattern, text, flags)
    return match.group(1).strip() if match else None
