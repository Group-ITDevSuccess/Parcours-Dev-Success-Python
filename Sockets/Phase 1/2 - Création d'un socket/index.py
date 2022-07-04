# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 17:32:40 2022

@author: Muriel
"""

from socket import *

s = socket()
print(s.getsockname())

t = socket(socket.AF_INET6, socket.SOCK_DGRAM)
print(t.getsockname())