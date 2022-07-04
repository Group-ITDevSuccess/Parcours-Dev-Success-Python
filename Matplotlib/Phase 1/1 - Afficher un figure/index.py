# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 23:16:57 2022

@author: Muriel
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3*np.pi, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

#Sauvegarder le figure
plt.savefig("fig.pdf")

plt.show()