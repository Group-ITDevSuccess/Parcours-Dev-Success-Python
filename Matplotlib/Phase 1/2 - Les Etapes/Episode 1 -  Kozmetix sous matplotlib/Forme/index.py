# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 23:50:02 2022

@author: Muriel
"""
import matplotlib.pyplot as plt
from numpy import *

x = linspace(0, 3*pi, 30)

#Image1.png
#☻plt.plot(x, sin(x), "o")

#Image2.png
plt.plot(x, (tan(x)/cos(x)), "g",
         markersize=15,
         markerfacecolor="pink",
         markeredgecolor="gray",
         markeredgewidth=5)

plt.savefig("image7.png")

plt.show()
