import json

from DatabaseHandlers import DeviceAuthenticationHandler
from DatabaseHandlers import DeviceDataHandler

from flask import request
from flask import Response
from flask import jsonify

class DeviceDataController:
	# Constructor
	def __init__(self):
		self.deviceAuth = DeviceAuthenticationHandler.DeviceAuthenticationHandler()
		self.deviceData = DeviceDataHandler.DeviceDataHandler()
		return

	# Handles post data
	def handleSensorData(self, request):
		# Not a POST
		if request.method != 'POST':
			return self.createErrorMessage(400, "No POST request")

		apikey = request.form['apikey']
		deviceId = request.form['deviceId']
		data = request.form['data']

		dataJsonObject = self.getJsonObject(data)

		# Checks if post data is empty
		if dataJsonObject == None or apikey == "" or deviceId == "":
			return self.createErrorMessage(400, "Not all POST parameters are set" + data + " " +deviceId)

		permission = self.deviceAuth.checkPermissionToPost(deviceId, apikey)	
		
		# Check permission
		if permission != "GRANTED":
			return self.createErrorMessage(403, permission) # if permission is a string it will contain a error message	

		result = self.deviceData.storeSensorData(data, deviceId)

		# If result contains something it contains an error
		if result is not None:
			return self.createErrorMessage(500, result)

		# Every check is passed so send a OK message back
		return self.createOkayMessage()

	#Checks if given string is able to convert to a JSON object
	# if not, returns None, if able, returns the JSON object		
	def getJsonObject(self, jsonText):
		try:
			jsonObject = json.loads(jsonText)
		except ValueError, e:
			return None
		return jsonObject	

	def createErrorMessage(self, errorCode, errorMessage):
		response = jsonify({'code' : errorCode, 'message' : errorMessage})
		response.status_code = errorCode
		return response

	def createOkayMessage(self):
		response = jsonify({'code' : 200, 'message' : 'OK'})
		response.status_code = 200
		return response		
