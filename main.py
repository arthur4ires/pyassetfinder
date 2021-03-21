import fontes.hackertarget
import fontes.ctrsh
import fontes.certspotter
import fontes.bufferoverun
import fontes.threatcrowd
import fontes.subdomainfinder

import sys
import socket
import argparse

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
	print("test")

if __name__ == "__main__":
	
	if sys.argv[1] != "":

		domainName = sys.argv[1]

		#printDomainList(fontes.hackertarget.returnDomains(domainName))
		#printDomainList(fontes.ctrsh.returnDomains(domainName))
		#printDomainList(fontes.certspotter.returnDomains(domainName))
		#printDomainList(fontes.bufferoverun.returnDomains(domainName))
		#printDomainList(fontes.threatcrowd.returnDomains(domainName))

		fontes.subdomainfinder.returnDomains(domainName)

		#print("\n".join(domainList))
		
		for domainAndIp in domainList:

			ipDomain =  getIpFromHostName(domainAndIp)

			print(domainAndIp,ipDomain)
	else:
		print("[+] Você deve setar o domínio!")
