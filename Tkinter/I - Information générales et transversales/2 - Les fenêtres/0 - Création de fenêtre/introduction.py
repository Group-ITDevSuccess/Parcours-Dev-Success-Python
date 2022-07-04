#-------------------------------------------------------------------------------
# Name:        Création d'un fenêtre et d'un widget
# Purpose:  Page 14 à 19
#
# Author:      Muriel
#
# Created:     11/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

#Ligne 18 :
"""
On importe toutes les fonctionnalités de Tkinter même si on n’a pas besoin de toutes
celles-ci
"""
from tkinter import *

WIDTH = 600
HEIGHT = 400

#Ligne 27 :
"""
On créé une fenêtre Tkinter en appelant le constructeur Tk, dite fenêtre «maîtresse »
(master)
"""
my_root = Tk()
#Ligne 30 :
"""
On crée un « canevas » dans la fenêtre : c’est un widget permettant d’effectuer du
graphisme, des animations, etc
"""
cnv = Canvas(my_root, width = WIDTH, height = HEIGHT, background='ivory')

#Ligne 39 :
"""
On indique avec pack comment le widget doit être intégré dans le widget-maître (ici
la fenêtre my_root)
"""
cnv.pack()

#Ligne 46:
"""
On lance la « boucle principale » (mainloop) de l’application. C’est typique de la
programmation événementielle.
"""
my_root.mainloop()