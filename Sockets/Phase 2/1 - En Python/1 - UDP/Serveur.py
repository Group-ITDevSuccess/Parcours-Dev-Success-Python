# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:52:55 2022

@author: Muriel
"""

#Etape 0 : Biblothèques à inclure
from socket import *

#Etape 1 : Création des descripteurs de la comminucation
s = socket(AF_INET, SOCK_DGRAM)

#Etape 2 : Réservation du port (coté serveur seul)
myAddress = '' #Ecouter sur toutes les interfaces reseau
myPort = 12345 #Port sur lequel écouter
s.bind((myAddress, myPort))

#Etape 3 : Le client envoie un datagrammer au serveur

#Etape 4 :  Le serveur reçoit le datagramme du client
message, sourceAddr = s.recvfrom(1024) #Récption, taille du tampon = 1024 octets

#Fin de communication
s.close()
