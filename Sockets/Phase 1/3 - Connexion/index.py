# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 17:37:17 2022

@author: Muriel
"""

from socket import *

s = socket()
s.connect(('www.python.org', 80))

print(s.getsockname())