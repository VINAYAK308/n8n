import re
import json
import argparse

# Define patterns and their labels
SENSITIVE_PATTERNS = {
    "SSN": r'\b\d{3}-\d{2}-\d{4}\b',
    "Visa Card": r'\b4[0-9]{12}(?:[0-9]{3})?\b',
    "Credit Card": r'\b(?:\d{4}[- ]?){3}\d{4}\b',
    "Aadhaar": r'\b\d{12}\b',
    "PAN": r'\b[A-Z]{5}[0-9]{4}[A-Z]\b',
    "Password": r'password\s*[:=]\s*\S+'
}

def is_sensitive(data):
    found_types = []
    for label, pattern in SENSITIVE_PATTERNS.items():
        match = re.search(pattern, data, re.IGNORECASE)
        if match:
            print(f"[!] Matched {label}: {match.group()}")
            found_types.append(label)
    return found_types

def main():
    parser = argparse.ArgumentParser(description="Check for sensitive data.")
    parser.add_argument('--input', default='processed_data.txt', help='Input file to scan')
    parser.add_argument('--output', default='sensitivity_flag.txt', help='Output file to store flag')
    parser.add_argument('--json_output', default='sensitivity_result.json', help='Optional JSON output file')
    args = parser.parse_args()

    try:
        with open(args.input) as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: {args.input} not found.")
        with open(args.output, 'w') as f:
            f.write('false')
        with open(args.json_output, 'w') as jf:
            json.dump({"sensitive": False, "types": []}, jf, indent=2)
        return

    detected = is_sensitive(data)
    is_sensitive_data = bool(detected)

    with open(args.output, 'w') as f:
        f.write('true' if is_sensitive_data else 'false')

    with open(args.json_output, 'w') as jf:
        json.dump({"sensitive": is_sensitive_data, "types": detected}, jf, indent=2)

    print(f"Sensitive: {is_sensitive_data}, Types: {detected}")

if __name__ == '__main__':
    main()
