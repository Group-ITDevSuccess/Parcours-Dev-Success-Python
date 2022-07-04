# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 17:27:39 2022

@author: Muriel
"""
import socket

#Domaine name
print(socket.getfqdn("www.google.be"))

#Non d'hote de la machine
print(socket.gethostname())

#Hôte à partir du nom
#print(socket.gethostbyname('www.google.be'))

#Hôte à partir de l'adresse
print(socket.gethostbyaddr('213.186.33.2'))