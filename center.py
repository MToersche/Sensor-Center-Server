import requests

from flask import Flask
from flask import Request
from flask import render_template
from flask import render_template_string

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('/pages/index.html',
						   title='Home',
						   )

@app.route('/post', methods=['POST'])
def post():
	error = None
	if request.method == 'POST':
		return request.form['deviceName']
	else:
		error = 'Invalid POST data'
		return error

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
