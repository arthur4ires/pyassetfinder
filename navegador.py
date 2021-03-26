import requests
import re

class Navegador:

	def __init__(self):
		self.url = ''
		self.typeResponse = ''
		self.sessionRequest = requests.Session()
		self.headerNavegador = {'accept-language': 'en-GB,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,en-US;q=0.6',
		             			'cache-control': 'no-cache',
		             			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36)'}

	def downloadResponse(self, url, typeResponse, method):

		self.sessionRequest.headers.update(self.headerNavegador)

		if typeResponse == 'JSON':

			try:
				return self.sessionRequest.get(url).json()
			except:
				return self.sessionRequest.get(url)

		elif typeResponse == 'HTML':

			return self.sessionRequest.get(url).text

		else:

			return self.sessionRequest.get(url, timeout=3) #status_code
	
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
