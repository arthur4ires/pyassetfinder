import navegador

URL_API = 'https://dns.bufferover.run/dns?q={}'
DOMAINS_LIST = []

def returnDomains(domainName):

	browserRequest = navegador.Navegador()
	
	jsonResponse = browserRequest.downloadResponse(URL_API.format(domainName),'JSON','GET')
	
	if jsonResponse['FDNS_A'] == NoneType:
		return []

	for _ in jsonResponse['FDNS_A']:

		domainIp, domainName  = _.split(',')

		DOMAINS_LIST.append(browserRequest.filterUrl(domainName))

	return DOMAINS_LIST
