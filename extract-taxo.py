#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print "Getting french translations..."


print "...from INPN"

TRANS = {} ##translations in french
with open("../Data/INPN/TAXREFv13.txt") as f:  
	next(f) ##skip header
	for line in f:
		sciname = line.split("\t")[14]
		comnameFR = line.split("\t")[19]
		if (comnameFR!=''):
			if (TRANS.has_key(sciname)==True):
				TRANS[sciname].append(comnameFR)
			else: 
				TRANS[sciname] = [comnameFR]


print "...from GBIF"

TAXONID = {}
#TRANS2 = {}
with open("../Data/GBIF/VernacularName.tsv") as f:  
	for line in f:
		taxonid = line.split("\t")[0]
		language = line.split("\t")[2]
		comname = line.split("\t")[1]
		line.split("\t")[1]
		if (language=='fr'):
			if (TAXONID.has_key(taxonid)==True):
				TAXONID[taxonid].append(comname)
			else: 
				TAXONID[taxonid] = [comname]

with open("../Data/GBIF/Taxon.tsv") as f:  
	for line in f:
		taxonid = line.split("\t")[0]
		sciname = line.split("\t")[7]
		if (TAXONID.has_key(taxonid)==True):
			if (TRANS.has_key(sciname)==True):
				TRANS[sciname].append(TAXONID[taxonid])
			else:
				TRANS[sciname] = TAXONID[taxonid]



print "...from Wikidata"

#TRANS3 = {}
with open("../Data/WikiData/query.tsv") as f:  
	next(f)
	for line in f:
		sciname = line.split("\t")[0]
		comnameFR = line.split("\t")[1]
		if (TRANS.has_key(sciname)==True):
			TRANS[sciname].append(comnameFR)
		else: 
			TRANS[sciname] = [comnameFR]



