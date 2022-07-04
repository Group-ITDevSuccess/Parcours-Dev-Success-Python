# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:52:21 2022

@author: Muriel
"""

from pylab import *

figure(figsize=(8,5), dpi=80)
subplot(111)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plot(X, C, color="blue", linewidth=2.5, linestyle="-")

plot(X, S, color="red", linewidth=2.5, linestyle="-")

xlim(X.min()*1.1, X.max()*1.1)

xlim(C.min()*1.1, C.max()*1.1)

show()