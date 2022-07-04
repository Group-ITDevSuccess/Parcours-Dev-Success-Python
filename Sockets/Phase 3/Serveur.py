# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:43:41 2022

@author: Muriel
"""
from socket import *

s = socket()

s.bind((gethostname(), 5000)) #Identier le serveur via port 5000

s.setblocking(False)
s.listen(2)

while True:
    try:
        clientConnected, client_address = s.accept() #Récupere l'adresse du client connecté
        print(str(client_address) + " connecté.") #Afficher l'adresse du client distant
        print(clientConnected.recv(32))#Affiche les caractères reçus
        
        clientConnected.sendall(b"Salut client")
        
        clientConnected.close() #On se déconnecte quand on a terminé
    except:
        pass

print("Fin de communication")

