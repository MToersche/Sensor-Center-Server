from pymongo import MongoClient

class DeviceDataHandler:
	def __init__(self):
		client = MongoClient('mongodb://localhost:27017/')
		self.db = client['local']
		return

	def storeSensorData(self, dataToStore, deviceID):
		#check if given data is json text or json object
		try:
			jsonObject = json.loads(dataToStore)
		except ValueError, e:
			return "No valid json"

		#Sanitize data
		#needs way more checking. 
		# Like:
		#	what is in the json(For XSS attacks)
		#	if there are arrays in arrays etc
		#	Did the correct tags get used
		data = {"deviceID":deviceID, "data":dataToStore}

		#If the data already exists, update the current data or else just save it
		deviceData = self.db.deviceData
		deviceData.update({"deviceID":deviceID}, data, true)

		return