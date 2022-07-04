# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 23:57:49 2022

@author: Muriel
"""

import matplotlib.pyplot as plt
from numpy import *

x = linspace(0, 3*pi, 30)

for marker in ["o", ".", ",", "x", "+", "v", "^", "<", ">", "s", "d"]:
    plt.plot(random.rand(10), random.rand(10), marker)
    #plt.savefig("Image.png")

plt.show()