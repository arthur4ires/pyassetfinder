import fontes.hackertarget
import fontes.ctrsh
import fontes.certspotter
import fontes.bufferoverun
import fontes.threatcrowd
import fontes.subdomainfinder

import sys
import socket
import argparse
import navegador

domainList = []

def getIpFromHostName(domain):
	try:
		return socket.gethostbyname(domain)
	except:
		return "0.0.0.0"

def addListToGlobal(listOld):

	global domainList

	for _ in listOld:

  		domainList.append(_)

	domainList = list(dict.fromkeys(domainList))

def printDomainList(domainList):

	#print("\n".join(domainList))

	addListToGlobal(domainList)

def argParserCommands():

	parser = argparse.ArgumentParser()
	parser.add_argument('-u','--url', dest="domainName", help='Você deve setar o domínio a ser pesquisado!', required=True)
	parser.add_argument('--status-code', dest="statusCode", help='Verifica se exister um servidor web e se ele está respondendo!', default=False, action="store_true")
	parser.add_argument('--ip-block', dest="ipBlock", help='Não exibe domínios com um IP específico!', default=False)
	parser.add_argument('--dev-mode', dest="debugName", help='APIs em desenvolvimento!', default=False, action="store_true")

	return parser.parse_args()

if __name__ == "__main__":
	
	returnComands = argParserCommands()


	if returnComands.debugName == False:

		printDomainList(fontes.hackertarget.returnDomains(returnComands.domainName))
		printDomainList(fontes.ctrsh.returnDomains(returnComands.domainName))
		printDomainList(fontes.certspotter.returnDomains(returnComands.domainName))
		printDomainList(fontes.bufferoverun.returnDomains(returnComands.domainName))
		printDomainList(fontes.threatcrowd.returnDomains(returnComands.domainName))

	else:

		fontes.subdomainfinder.returnDomains(returnComands.domainName)
	
	for domainAndIp in domainList:

		ipDomain =  getIpFromHostName(domainAndIp)
		
		if returnComands.ipBlock != False and returnComands.ipBlock == ipDomain:
			continue

		domainReturn = domainAndIp

		if returnComands.statusCode != False:
			try:
				statusCode = navegador.Navegador().downloadResponse('http://{}'.format(domainAndIp),'STATUS','GET').status_code
			except:
				statusCode = 'TIMEOUT'
			
			if statusCode != None:
				domainReturn += ' - ({})'.format(statusCode)
		
		domainReturn += ' {}'.format(ipDomain)

		print(domainReturn)