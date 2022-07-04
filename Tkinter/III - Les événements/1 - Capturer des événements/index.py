#-------------------------------------------------------------------------------
# Name:        Capturer des événements
# Purpose:
#
# Author:      Muriel
#
# Created:     16/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

def f(event):
    t = event.keysym
    print("Touche pressé : ", t)
"""
Lorsqu'on presse une touche du clavier, la fonction f reçoit l'événement
correspondant. Cet événements, appelé ici event (mais qu'on pourrait appeler
par tout autre nom) est n objet dont un des attributs keysym est le nom de la
touche sur laquelle on appuyé. La fonction f affiche le nom de cette touche.
"""
#f et g sont dites des fonctions de rappel (en anglais, callback function)
def g(event):
    x = event.x
    y = event.y
    print("Position : ",x, y)
"""
Lorsque la souris bouge, la fonction g recoit l'événement correspondant. Cet
événement est un objet dont les attributs x et y représentent la position courant
de la souris. La fonction g affiche alors cette possition.

"""
root = Tk()
root.title("Le capture des événements")

root.bind("<Key>",f)
"""
La chaîne "<Key>" représente l'evenement de pression quelconque sur une touche
de clavier. Cette ligne de code lie(bind en anglais) la fonction f définie et ces
événememts. Chaque fois qu'un tel événements se produit, la fonction f est exécutée.

"""

root.bind("<Motion>",g)
""""
La chaîne "<Motion>" représente l'évenement de déplacement de la souris dans la
fenêtre. Chaque point de la fenêtre root a une position exprimée en pixels.
La position du coin supérieur gauche est (0,0). Cette ligne de code lie la fonction g
définie et ces déplacement. Chaque fois que la souries bouge, la fonction g
est exécutée.

"""
root.mainloop()