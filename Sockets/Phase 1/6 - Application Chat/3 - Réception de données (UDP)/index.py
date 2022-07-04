# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:53:50 2022

@author: Muriel
"""

from socket import *

s = socket(type= SOCK_DGRAM)
s.bind((gethostname(), 5000))

data = s.recvfrom(512).decode()

print('Reçu ', len(data), 'octets : ')
print(data)

s.close()