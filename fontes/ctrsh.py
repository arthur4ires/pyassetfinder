import navegador

URL_API = 'https://crt.sh/?q={}&output=json'
DOMAINS_LIST = []

def returnDomains(domainName):

	browserRequest = navegador.Navegador()
	
	jsonResponse = browserRequest.downloadResponse(URL_API.format(domainName),'JSON','GET')

	for _ in jsonResponse:

		if "*." in _['common_name']:
			stringAppend = _['common_name'].replace('*.','')
		elif '\\n' in _['common_name']:
			stringAppend = _['common_name'].replace('\\n','')
		else:
			stringAppend = _['common_name']
			
		DOMAINS_LIST.append(stringAppend)

	return DOMAINS_LIST