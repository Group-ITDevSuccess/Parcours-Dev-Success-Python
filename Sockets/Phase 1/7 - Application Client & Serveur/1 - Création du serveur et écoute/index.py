# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:28:36 2022

@author: Muriel
"""
#=========================================================================
#                               Machine Serveur
#=========================================================================

from socket import *

s = socket()
"""
s.bind((gethostname(), 6000))

s.listen()
client, addr = s.accept()
"""
s.connect((gethostname(), 6000))

data = s.recv(512).decode()

print('Recu', len(data), 'octets : ')
print(data)

s.close()