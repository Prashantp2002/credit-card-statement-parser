import sys
from utils.pdf_reader import extract_text
from utils.issuer_detector import detect_issuer

from parsers import hdfc, icici, sbi, axis, citibank

PARSERS = {
    "HDFC": hdfc,
    "ICICI": icici,
    "SBI": sbi,
    "Axis": axis,
    "Citibank": citibank
}

if len(sys.argv) < 2:
    print("Usage: python main.py <pdf_path>")
    sys.exit(1)

pdf_path = sys.argv[1]
text = extract_text(pdf_path)
issuer = detect_issuer(text)

if issuer in PARSERS:
    print(PARSERS[issuer].parse(text))
else:
    print("Unsupported issuer")
