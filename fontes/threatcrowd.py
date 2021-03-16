import navegador

URL_API = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}'
DOMAINS_LIST = []

def returnDomains(domainName):

	browserRequest = navegador.Navegador()
	
	jsonResponse = browserRequest.downloadResponse(URL_API.format(domainName),'JSON','GET')

	for _ in jsonResponse['subdomains']:

		DOMAINS_LIST.append(browserRequest.filterUrl(_))

	return DOMAINS_LIST