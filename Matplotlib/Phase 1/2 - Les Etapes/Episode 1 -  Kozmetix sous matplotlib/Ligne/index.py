# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 00:03:36 2022

@author: Muriel
"""

import matplotlib.pyplot as plt
from numpy import *

x = linspace(0, 3*pi, 30)

#Image1.png
plt.plot(x, x +0, "-og")

#Image2.png
plt.plot(x, x +1, "--xc")

#Image3.png
plt.plot(x, x +2, "-..k")

#Image4.png
plt.plot(x, x +3, ":sr")

plt.savefig("Image4.png")

plt.show()
