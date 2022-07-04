# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:49:57 2022

@author: Muriel
"""

from socket import *


s = socket(type=SOCK_DGRAM)

address = ('localhost', 5000)
message = "Salam Alaikum Muriel".encode()

totalsent = 0
while totalsent < len(message):
    sent = s.sendto(message[totalsent:], address)
    totalsent += sent

s.close()