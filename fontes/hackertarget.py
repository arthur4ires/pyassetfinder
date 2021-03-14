import navegador

URL_API = 'https://api.hackertarget.com/hostsearch/?q={}'
DOMAINS_LIST = []

def returnDomains(domainName):

	browserRequest = navegador.Navegador()
	
	htmlResponse = browserRequest.downloadResponse(URL_API.format(domainName),'HTML','GET').split(',')

	DOMAINS_LIST.append(htmlResponse[0])

	return DOMAINS_LIST