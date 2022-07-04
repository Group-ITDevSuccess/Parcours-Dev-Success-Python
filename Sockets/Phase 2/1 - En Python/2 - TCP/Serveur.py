# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:13:27 2022

@author: Muriel
"""
from socket import *

#Etape 1 : Création des descripteurs de la communication
s = socket(AF_INET, SOCK_STREAM)

#Etape 2 : Enregistrement aupères du système d'exploitation (Serveur)
myAddress = ''
myPort = 12345
s.bind((myAddress, myPort))

#Etape 3 : Déclaration du nombre maximal de connexions acceptées (Serveur)
s.listen(5)

#Etape 4 : Attente de connexions (Serveur)
sData, senderAddress = s.accept()

#Etape 5 : Connexion du client(Client) 
messageRecu = sData.recv(1024)

s.close()