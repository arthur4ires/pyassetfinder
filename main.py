import fontes.hackertarget
import fontes.ctrsh
import fontes.certspotter
import fontes.bufferoverun

if __name__ == "__main__":
	
	print(fontes.hackertarget.returnDomains('httpbin.org'))
	print(fontes.ctrsh.returnDomains('httpbin.org'))
	print(fontes.certspotter.returnDomains('httpbin.org'))
	print(fontes.bufferoverun.returnDomains('httpbin.org'))