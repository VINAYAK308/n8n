def preprocess():
    with open('scanned_data.txt') as f:
        data = f.read()
    # Preprocess data
    processed = data.strip().lower()
    with open('processed_data.txt', 'w') as f:
        f.write(processed)

if __name__ == '__main__':
    preprocess()