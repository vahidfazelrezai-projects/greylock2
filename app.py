from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/blah/')
@app.route('/blah/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)