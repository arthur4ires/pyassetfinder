import navegador

URL_API = "https://api.hackertarget.com/hostsearch/?q={}"

def returnDomains(domainName):
	
	browserRequest = navegador.Navegador()
	print(browserRequest.downloadResponse(URL_API.format(domainName),'GET','HTML'))