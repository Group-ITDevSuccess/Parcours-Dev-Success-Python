# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:13:42 2022

@author: Muriel
"""

from socket import *

#Etape 1 : Création des descripteurs de la communication
s = socket(AF_INET, SOCK_STREAM)

#Etape 2 : Enregistrement aupères du système d'exploitation (Serveur)

#Etape 3 : Déclaration du nombre maximal de connexions acceptées (Serveur)

#Etape 4 : Attente de connexions (Serveur)

#Etape 5 : Connexion du client(Client)
destIPAddr = "localhost"
destIPPort = 12345
s.connect((destIPAddr, destIPPort))

#Etape 6 : Emission de données (Client)
sData.send("Salut")

s.close()

