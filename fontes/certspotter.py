import navegador

URL_API = 'https://api.certspotter.com/v1/issuances?domain={}&expand=dns_names&expand=issuer'
DOMAINS_LIST = []

def returnDomains(domainName):

	browserRequest = navegador.Navegador()
	
	jsonResponse = browserRequest.downloadResponse(URL_API.format(domainName),'JSON','GET')
	
	if jsonResponse['code'] == "not_allowed_by_plan":
		return []

	for _ in jsonResponse:

		for __ in _['dns_names']:
			DOMAINS_LIST.append(browserRequest.filterUrl(__))

	return DOMAINS_LIST
