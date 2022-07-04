# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:33:57 2022

@author: Muriel
"""

"""
Nous voudrons tracer les fonctions sinus et cosinus sur un seul et même graphique.
"""
from pylab import *

n = 256
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

C, S = np.cos(X), np.sin(X)
plot(X,C) 
plot(X,S)

show()