from flask import Flask, Response, render_template
from prometheus_client import Counter, generate_latest
import os

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('web_requests_total', 'Total number of web requests')

@app.route('/')
def index():
    REQUEST_COUNT.inc()
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
