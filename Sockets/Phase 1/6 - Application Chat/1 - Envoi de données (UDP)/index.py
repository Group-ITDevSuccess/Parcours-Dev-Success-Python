# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:44:50 2022

@author: Muriel
"""

from socket import *

s = socket(type=SOCK_DGRAM)

address = ('localhost', 5000)

data = "Salam Alaikum Muriel".encode()

sent = s.sendto(data, address)
if sent == len(data):
    print("Envoi complet !")

s.close()