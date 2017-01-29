__author__ = 'pshort'

from Bio import Entrez

Entrez.email = "pjshort42@gmail.com"

def EntrezSearch(rsid):
	handle = Entrez.esearch(db="pmc", term=rsid)
	record = Entrez.read(handle)
	print(record["IdList"])
	return(record["IdList"])

if __name__ == "__main__":
	EntrezSearch("rs7412")
	EntrezSearch("rs11540652")
	EntrezSearch("rs121912652")
	EntrezSearch("rs121912653")
	EntrezSearch("rs72921001")