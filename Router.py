import requests

from Controllers import DeviceDataController

from flask import Flask
from flask import request
from flask import render_template
from flask import render_template_string

class Router:

	def __init__(self):
		return

	def run(self):
		app = Flask(__name__)

		@app.route('/')
		def index():
			return render_template('/home/pi/Sensor-Center-Server/templates/pages/index.html', title='Home')

		##Post data
		#Expects:	apikey - string
		#			deviceName - string
		#			data - array with:
		#				title:[text] - gets shown as a title
		#				paragraph:[text] - gets shown as a block of text
		@app.route('/store', methods=['POST'])
		def storeSensorData():
			dataHandler = DeviceDataController.DeviceDataController()
			response = dataHandler.handleSensorData(request)
			return response

		#if __name__ == '__main__':
		app.run(debug=True, host='0.0.0.0')
