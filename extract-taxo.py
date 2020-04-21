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
		comnameFR = line.split("\t")[19] ##remove unwanted caracters (\n,\t,\r, space at the end, etc.)
		#remove (Le) and (La) and (L') for compatibility with other database
		comnameFR = comnameFR.replace("(L')","").replace("(Le)","").replace("(La)","")
		## cut multiple names separatated by coma (,) into multiple list elements
		comnameFR = comnameFR.split(",")
		comnameFR = [x.rstrip().lstrip() for x in comnameFR]
		if (comnameFR!=''):
			if (TRANS.has_key(sciname)==True):
				TRANS[sciname].extend(comnameFR)
			else: 
				TRANS[sciname] = comnameFR


print "...from GBIF"

TAXONID = {}
#TRANS2 = {}
with open("../Data/GBIF/VernacularName.tsv") as f:  
	for line in f:
		taxonid = line.split("\t")[0]
		language = line.split("\t")[2]
		comname = line.split("\t")[1].rstrip()
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
				TRANS[sciname].extend(TAXONID[taxonid])
			else:
				TRANS[sciname] = TAXONID[taxonid]



print "...from Wikidata"

#TRANS3 = {}
with open("../Data/WikiData/query.tsv") as f:  
	next(f)
	for line in f:
		sciname = line.split("\t")[0]
		comnameFR = line.split("\t")[1].rstrip()
		if (TRANS.has_key(sciname)==True):
			TRANS[sciname].append(comnameFR)
		else: 
			TRANS[sciname] = [comnameFR]



def sortlistbasedonlist(list1, list2):
	zipped_lists = zip(list2, list1)
	sorted_zipped_lists = sorted(zipped_lists)
	sorted_list1 = [element for _, element in sorted_zipped_lists]
	return sorted_list1


print "Writing output file and removing duplicates..."

fi = open('taxo-vernac-FR.txt', 'w')

for k in sorted(TRANS.keys()):
	NumOfUpper = [sum(1 for c in w if c.isupper()) for w in TRANS[k]] ##number of uppercase letters in each name
	reorderdlist = sortlistbasedonlist(TRANS[k], NumOfUpper)
	reorderdlist_lower = [x.lower() for x in reorderdlist]
	## the following filter allows keeping the common name
	## with the more uppercase letters in case of duplication (modulo upper-cases)
	for i in range(len(reorderdlist_lower)): ##removes duplicates
		if (reorderdlist_lower[i] not in reorderdlist_lower[(i+1):]):
			fi.write(k + "\t" + reorderdlist[i] + "\n")
fi.close()
