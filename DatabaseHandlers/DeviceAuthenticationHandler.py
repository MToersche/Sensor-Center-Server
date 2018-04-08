import datetime
import hashlib

from pymongo import MongoClient

class DeviceAuthenticationHandler:
	def __init__(self):
		client = MongoClient('mongodb://localhost:27017/')
		self.db = client['local']
		return

	def checkPermissionToPost(self, deviceID, apikey):
		#Get record based off the deviceId
		authorizedDevices = self.db.authorizedDevices
		foundDevice = authorizedDevices.find_one({"deviceID":deviceID})

		#If device ID doesnt excist return not found
		if foundDevice == None
			return "Device not found"

		#If given apikey doesnt equals stored api key return error
		if foundDevice.apikey != apikey
			return "Invalid API key"

		#Returns granted when apikey equels stored apikey
		return "GRANTED" # returns granted if the sensor is authenticated

	def generateApiKey(self, deviceID):
		# generate an apikey
		date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		hashObject = hashlib.md5(date.encode())
		apikey = hashObject.hexdigest()

		if apikey == None
			return "FAILED"

		return apikey # return generated apikey

	def storeApiKey(self, deviceID, apikey):
		# Check if deviceID already exist
		authorizedDevices = self.db.authorizedDevices
		foundDevice = authorizedDevices.find_one({"deviceID":deviceID})

		if foundDevice != None
			return "Device already exist"

		# store apikey with device ID in mongoDB
		result = authorizedDevices.insert_one({"deviceID":deviceID, "apikey":apikey})

		if result.upserted_id == None
			return "Insertion of apikey failed"

		return "Insertion completed"