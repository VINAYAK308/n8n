from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/trigger', methods=['GET'])
def trigger_workflow():
    subprocess.run(['python3', 'watcher.py'])
    return 'Workflow triggered', 200

if __name__ == '__main__':
    app.run(port=5000)