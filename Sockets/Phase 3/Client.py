# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:43:50 2022

@author: Muriel
"""

from socket import *

s = socket() #Création de l'instance
s.setblocking(False) #En mode non bloquant c'est mieu
s.connect((gethostname(), 5000)) #Spécifie l'adresse IP du serveur via port 5000

s.sendall("Salam Alaikum Muriel") #Envoi de message
print(s.recv(32)) #Afficher le reponse reçu
s.close()
print("Fin de la communication")
