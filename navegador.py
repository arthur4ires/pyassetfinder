import requests


class Navegador:

	def __init__(self):
		self.url = ''
		self.typeResponse = ''
		self.sessionRequest = requests.Session()

	def downloadResponse(self, url, typeResponse, method):

		if typeResponse == 'json':
			return self.sessionRequest.get(url).json
		else:
			return self.sessionRequest.get(url)
