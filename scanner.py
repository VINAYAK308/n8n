def scan():
    # Scan logic here
    print("Scanning data...")
    # Pass data to next step (could write to file or use IPC)
    with open('scanned_data.txt', 'w') as f:
        f.write("Credit Card: 1234-5678-9882-7897")

if __name__ == '__main__':
    scan()