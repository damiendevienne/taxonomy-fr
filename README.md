
# Goal of this project
The aim of this repository is to propose an up-to-date correspondance between latin and vernacular french names for as many taxa as possible. This is used in lifemap-fr. 


# Data sources and retrieval strategies
**1. Wikidata**


Wikidata is a great resource for species names translation. The following code (Sparkle) can be used to retrieve the common names of taxons in french. Simply copy-paste it here: [https://query.wikidata.org](https://query.wikidata.org/) 
```
SELECT DISTINCT ?sci ?comm ?link WHERE {
  ?taxon wdt:P31 wd:Q16521;
    wdt:P225 ?sci;
    wdt:P1843 ?comm.
  OPTIONAL {
    ?link schema:about ?taxon;
    schema:isPartOf <https://fr.wikipedia.org/>.
  }
  FILTER(LANGMATCHES(LANG(?comm), "fr"))
  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr". }
} 
```
This allows retrieving 24049 common names (as of April, 19 2020) covering xxxxx unique taxa	

**2. GBIF**


GBIF contains vernacular names for many species in many languages. A single zip file can be downloaded here : 
http://rs.gbif.org/datasets/backbone/backbone-current.zip
From there, you can retrieve a file called : 
`VernacularName.tsv`
and another one called 
`Taxon.tsv`
From there you can make the correct file 




**3. INPN**


The INPN is a great resource for species names of species living in France (but not the others). The complete data can be downloaded from https://inpn.mnhn.fr/docs-web/docs/download/301786




