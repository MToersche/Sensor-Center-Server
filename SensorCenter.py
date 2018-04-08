import Router

class SensorServer:
	def __init__(self):
		route = Router.Router()
		route.run()

sensorServer = SensorServer()