import datetime

def log_to_rms():
    with open('masked_data.txt') as f:
        data = f.read()
    timestamp = datetime.datetime.now().isoformat()
    with open('rms_log.txt', 'a') as log:
        log.write(f"{timestamp} | {data}\n")
    print("Logging to RMS...")

if __name__ == '__main__':
    log_to_rms()