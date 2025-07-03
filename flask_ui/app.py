from flask import Flask, render_template
from rule_engine.rules import run_detection
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    alerts = run_detection('log_collector/custom.log')
    return render_template('index.html', alerts=alerts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
