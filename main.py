import subprocess

# Run watcher.py
subprocess.run(['python3', 'watcher.py'])

# Run scanner.py
subprocess.run(['python3', 'scanner.py'])

# Run preprocessing.py
subprocess.run(['python3', 'preprocessing.py'])

# Run sensitivity_check.py
subprocess.run(['python3', 'sensitivity_check.py'])

# Read the sensitivity flag to decide the next step
with open('sensitivity_flag.txt') as f:
    flag = f.read().strip()

if flag == 'true':
    subprocess.run(['python3', 'apply_rules.py'])
    subprocess.run(['python3', 'send_to_ai_ml.py'])

# Continue with loglistener.py, log_to_rms.py, gui_output.py
subprocess.run(['python3', 'loglistener.py'])
subprocess.run(['python3', 'log_to_rms.py'])
subprocess.run(['python3', 'gui_output.py'])