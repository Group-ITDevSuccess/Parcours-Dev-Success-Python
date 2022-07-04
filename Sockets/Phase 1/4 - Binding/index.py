# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:39:27 2022

@author: Muriel
"""

from socket import *

s = socket()

s.bind((gethostname(), 6000))

print(s.getsockname())
