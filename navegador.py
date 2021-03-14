import requests


class Navegador:

	def __init__(self):
		self.url = ''
		self.typeResponse = ''
		self.sessionRequest = requests.Session()

	def downloadResponse(self, url, typeResponse, method):

		if typeResponse == 'JSON':

			return self.sessionRequest.get(url).json()

		elif typeResponse == 'HTML':

			return self.sessionRequest.get(url).text

		else:

			return self.sessionRequest.get(url)
