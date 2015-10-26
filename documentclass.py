#-*- coding: UTF-8 -*-
import glob, os.path, sys, re
from datetime import datetime

class document:
	"classe document qui permettra de décrire les attributs et les méthodes liées à un document"
	
	def __init__(self, url):
        "construit une instance avec les attributs de base ie adresse"
        self.url = url

	def get_format(self):
		"retourne l'extension du nom de fichier permettant d'avoir une idée du format du document"
		return self.url
		
	def tokenize(self, chaine, lang='fr'):
		"retourne une liste chaine segmentée en mots, phrases et paragraphes"
		