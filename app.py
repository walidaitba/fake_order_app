from flask import Flask, render_template, request, jsonify
import subprocess
import sys
import os
import signal

app = Flask(__name__)

# Global variables to track script status
script_process = None
submission_count = 0
is_paused = False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_script():
    global script_process, submission_count
    data = request.json
    url = data['url']
    delay = data['delay']
    
    if script_process is None:
        # Start the form filler script with parameters
        script_process = subprocess.Popen(
            [sys.executable, 'fake_order.py', url, str(delay)],
            env=dict(os.environ, PYTHONUNBUFFERED="1")
        )
        submission_count = 0
        return jsonify({"status": "started"})
    return jsonify({"status": "already_running"})

@app.route('/pause', methods=['POST'])
def pause_script():
    global is_paused
    data = request.json
    is_paused = data.get('paused', False)
    return jsonify({"status": "paused" if is_paused else "resumed"})

@app.route('/status')
def get_status():
    global submission_count
    return jsonify({"count": submission_count})

@app.route('/submission', methods=['POST'])
def update_submission_count():
    global submission_count
    submission_count += 1
    return jsonify({"status": "updated"})

if __name__ == '__main__':
    app.run(debug=True)
