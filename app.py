from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Main route to load the IDE
@app.route('/')
def index():
    return
render_template

# Endpoint to execute Python code
@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code') # Get the code from the request

    try:
        # Use subprocess to execute the code safely
        result = subprocess.run(['python3', '-c', code], capture_output=True, text=True, timeout = 5)
	    output = result.stdout
if result.returncode == 0 else result.stderr
	except Exception as e:
		output = str(e)
            
    return jsonify({'output':output})

    if __name__ == '__main__':
        app.run(debug=True)