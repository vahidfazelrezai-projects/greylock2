from flask import Flask, request
import requests
import urllib

app = Flask(__name__)

s = requests.Session()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<url>')
def browse(url=None):
    print url
    return url
    # url = urllib.unquote(url).decode('utf8')
    # return url.split(':')[0]
    # r = s.get()
    # return r.content
