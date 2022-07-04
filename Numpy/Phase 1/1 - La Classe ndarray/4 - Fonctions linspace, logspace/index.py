# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 23:15:49 2022

@author: Muriel
"""

from numpy import *

m1 = linspace(0, 10, 5) #start, stop, number of pointts
print(m1)

m2 = logspace(1, 2, 4) # 4 points between 10**1 and 10**2
print(m2)

m2 = logspace(1, 2, 4, base=2) # 4 points between 2**1 and 2**2
print(m2)