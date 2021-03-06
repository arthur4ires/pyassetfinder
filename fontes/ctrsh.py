import navegador

URL_API = 'https://crt.sh/?q={}&output=json'
DOMAINS_LIST = []

def returnDomains(domainName):

	browserRequest = navegador.Navegador()
	
	jsonResponse = browserRequest.downloadResponse(URL_API.format(domainName),'JSON','GET')

	for _ in jsonResponse:
			
		DOMAINS_LIST.append(browserRequest.filterUrl(_['common_name']))

	return DOMAINS_LIST