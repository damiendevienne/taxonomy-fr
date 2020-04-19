# Trying to centralise the largest possible list of vernacular names in french

# Sources and retrieval strategies
1. Wikidata
Wikidata is a great resource for species names translation. The following code (Sparkle) can be used to retrieve the common names of taxons in french. 

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
2. GBIF
A single file can be downloaded to get the whole backbone taxonomy of GBIF: 
http://rs.gbif.org/datasets/backbone/backbone-current-simple.txt.gz

3. INPN
The INPN is a great resource for species names of species living in France (but not the others). The complete data can be downloaded from https://inpn.mnhn.fr/docs-web/docs/download/301786



