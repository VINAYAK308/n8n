import re
import logging
import argparse

# Setup logging
logging.basicConfig(filename='apply_rules.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def mask_sensitive(data: str) -> str:
    """Mask sensitive information in the data."""
    # Credit Card: 16 digits (e.g., 1234-5678-9012-3456 or 1234567890123456)
    data = re.sub(r'\b(\d{4})[- ]?(\d{4})[- ]?(\d{4})[- ]?(\d{4})\b', r'****-****-****-\4', data)

    # Aadhaar Number: 12 digits (e.g., 1234 5678 9012 or 123456789012)
    data = re.sub(r'\b(\d{4})[ ]?(\d{4})[ ]?(\d{4})\b', r'**** **** \3', data)

    # PAN Number: 5 uppercase letters, 4 digits, 1 uppercase letter (e.g., ABCDE1234F)
    data = re.sub(r'\b([A-Z]{5})([0-9]{4})([A-Z])\b', r'*****\2\3', data)

    # API Keys: e.g., API_KEY_ABCDEF1234567890ABCDEF1234567890
    data = re.sub(r'\bAPI_KEY_[A-Za-z0-9]{32,}\b', r'API_KEY_****************', data)

    return data

def process_file(input_path: str, output_path: str):
    try:
        with open(input_path, 'r') as infile:
            data = infile.read()
        masked = mask_sensitive(data)
        with open(output_path, 'w') as outfile:
            outfile.write(masked)
        logging.info(f"Masked data written to {output_path}")
        print(f"Masked data written to {output_path}")
    except FileNotFoundError:
        logging.error(f"Input file not found: {input_path}")
        print(f"Error: Input file not found: {input_path}")
    except Exception as e:
        logging.error(f"Error in apply_rules: {e}")
        print(f"Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Apply masking rules to sensitive data.")
    parser.add_argument('--input', type=str, default='scanned_data.txt', help='Input file with sensitive data')
    parser.add_argument('--output', type=str, default='masked_data.txt', help='Output file for masked data')
    args = parser.parse_args()

    process_file(args.input, args.output)
