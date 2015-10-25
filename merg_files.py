#-*- coding: UTF-8 -*-
import glob, os.path, sys, re
from datetime import datetime

#  on liste les fichiers dans un repertoire donne (recherche egalement sous-rep)
liste_files = glob.glob(sys.argv[1] + '/*/*')
print len(liste_files)
corpus={} ## structure d 'accueil des corpus par mois
# corpus[year-date]=[liste des fichiers, taille totale]

# on parcoure chacun des fichiers et on affiche les metadonnees
for f in liste_files:
	sizef= int(os.path.getsize(f)) # taille du fichier
	mtime = os.path.getmtime(f) # date creation du fichier
	timestp = str(datetime.fromtimestamp(mtime)) # date plus lisible
	yearmonth = timestp.split("-") # on recupere annee + mois qui sert de cle
	try: # on recupere la valeur - liste si la cle existe
		listdata = corpus[yearmonth[0]+ "-" +yearmonth[1]]
		listfiles = listdata[0]
		size=listdata[1]
	except KeyError: # pas de cle : on initialise la valeur liste
		listfiles = []
		size = 0
		listdata = [listfiles,size]
	listfiles.append(f) # on ajoute le fichier a la liste
	size = size + sizef # on additionne la taille du fichier courant a la taille totale des fichiers de cette liste
	corpus[yearmonth[0]+ "-" +yearmonth[1]]=[listfiles, size]


# ecriture des resultats + creation des fichiers par mois
for key in corpus:
	print key + ":"
	data = corpus[key]
	print int(data[1])
	print len(data[0])
	# on ouvre le fichier en mode 'a' comme append - ou ajouter
	with open(key + ".txt", "a") as sortie:
		for f in data[0]:
			with open(f,"r") as input:
				contents = input.read()
        		sortie.write(contents)
	
		

