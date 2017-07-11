from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')

@app.route('/foundationexamples')
def foundation_examples():
    return render_template('oldindex.html')
