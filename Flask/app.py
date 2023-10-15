from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('Page1.html')

@app.route('/about')
def about():
    return render_template('Page2.html')