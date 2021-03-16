import navegador

URL_API = 'https://urlscan.io/api/v1/search/?q=domain:{}'
DOMAINS_LIST = []

#working

def returnDomains(domainName):

	browserRequest = navegador.Navegador()
	
	jsonResponse = browserRequest.downloadResponse(URL_API.format(domainName),'JSON','GET')

	return DOMAINS_LIST