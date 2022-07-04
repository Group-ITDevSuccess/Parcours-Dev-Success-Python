# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 23:24:25 2022

@author: Muriel
"""

import matplotlib.pyplot as plt
from numpy import *
x = linspace(0, 3*pi, 100)
"""
plt.plot(x, sin(x))
plt.plot(x, cos(x))
"""
#Pour image.png
plt.plot(x, x+0, linestyle="solid")
plt.plot(x, x+1, linestyle="dashed")
plt.plot(x, x+2, linestyle = "dashdot")
plt.plot(x, x+3, linestyle = "dotted")

#Pour imag1.png
plt.plot(x, sin(x -0), color="blue")

#Pour imag2.png raccourci (rgbcmyk)
plt.plot(x, sin(x -1), color="g")

#Pour imag3.png gris [0;1]
plt.plot(x, sin(x -2), color="0.75")

#Pour imag4.png
plt.plot(x, sin(x -3), color="#FFDD44")

#Pour imag5.png tuple[0;1]
plt.plot(x, sin(x -4), color=(1.0,0.2,0.3))

#Pour imag6.png Cycle de couleur C0-9
plt.plot(x, sin(x -4), color="C4")

plt.savefig("imag6.png")

plt.show()