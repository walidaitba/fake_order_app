from flask import Flask, render_template, request, jsonify
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_script():
    data = request.jsons
    url = data['url']
    delay = data['delay']
    
    # Start the form filler script with parameters
    subprocess.Popen([sys.executable, 'fake_oder.py', url, delay])
    return jsonify({"status": "started"})

if __name__ == '__main__':
    app.run(debug=True)
