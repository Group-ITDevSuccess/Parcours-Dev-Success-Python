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

host, port =('',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))

print("Le serveur est démarré...")

while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("Un client vient de se connecter..")
    
    data = conn.recv(1024)
    data = data.decode("utf-8")
    print(data)

conn.close()
socket.close()