from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('base.html')

@app.route('/content')
def content():
	return render_template('content.html')

app.run(debug=True)