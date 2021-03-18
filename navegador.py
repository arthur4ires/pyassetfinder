import requests
import re

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
	
	def urlValidator(self, url):
		regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

	def filterUrl(self, url):

		urlClean = url

		if "*." in url:
			urlClean = url.replace('*.','')
		
		if '\\n' in url:
			urlClean = url.replace('\\n','')

		return urlClean
