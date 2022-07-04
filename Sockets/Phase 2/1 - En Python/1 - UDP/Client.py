# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:59:23 2022

@author: Muriel
"""

#Etape 0 : Biblothèques à inclure
from socket import *

#Etape 1 : Création des descripteurs de la comminucation
s = socket(AF_INET, SOCK_DGRAM)

#Etape 2 : Réservation du port (coté serveur seul)

#Etape 3 : Le client envoie un datagrammer au serveur
destIPAddr = "localhost"
destPort = 12345
message = "Salam Alaikum Muriel \n"
s.sendto(message, (destIPAddr, destPort))

#Etape 4 :  Le serveur reçoit le datagramme du client

#Fin de communication
s.close()