# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:27:50 2022

@author: Muriel
"""
#=========================================================================
#                               Machine Client
#=========================================================================

from socket import *

s = socket()

s.connect((gethostname(), 6000))

data = "Salam Alaikum Muriel !".encode()
sent = s.send(data)
totalsent = 0

"""
if sent == len(data):
    print("Envoie complet")
"""  
while totalsent < len(data):
    sent = s.send(data[totalsent:])
    totalsent += sent

s.close()