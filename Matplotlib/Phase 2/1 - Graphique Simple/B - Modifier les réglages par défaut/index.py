# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:53:15 2022

@author: Muriel
"""
# on importe tout de matplotlib
# numpy est accessible via l'alias 'np'
from pylab import *

# on crée un graphique de 8x6 pouces
# avec une résolution de 80 points par pouce
figure(figsize=(8,6), dpi = 80)

# on crée une nouvelle vue dans une grille de 1 ligne x 1 colonne
subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# on trace la fonction cosinus en rouge avec un trait plein de 1 pixel d'épaisseur
plot(X, C, color="red", linewidth=1.0, linestyle="-")

# on trace la fonction sinus en vert avec un trait plein de 1 pixel d'épaisseu
plot(X, S, color="green", linewidth=1.0, linestyle="-")

# limites de l'axe (O,x) des abscisses
xlim(-4.0, 4.0)

# graduations de l'axe (O,x) des abscisses
xticks(np.linspace(-4, 4, 9, endpoint=True))

# limites de l'axe (O,y) des ordonnées
ylim(-1.0, 1.0)

# graduations de l'axe (O,y) des ordonnées
yticks(np.linspace(-1, 1, 5, endpoint=True))

# on affiche le résultat à l'écran
show()