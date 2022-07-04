# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Les sockets
# Purpose: Cours 33
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

host, port =('127.0.0.1',5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
    socket.connect((host, port))
    print("Client connecté")
    
    data = "Salam Alaikum, je suis Muriel : voici mes donnée !"
    data = data.encode("utf-8")
    socket.sendall(data)
except:
    print("Connexion au Serveur échouée !")
finally:
    socket.close()