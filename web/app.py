from flask import Flask, request
import requests
import urllib

app = Flask(__name__)

s = requests.Session()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def browse(path=None):
    path = urllib.unquote(path).decode('utf8')
    protocol = path.split(':')[0]
    if protocol not in ['http', 'https']:
        path = 'http://' + path
    print path
    r = s.get(path)
    return r.content
