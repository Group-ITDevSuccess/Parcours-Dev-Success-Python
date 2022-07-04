#-------------------------------------------------------------------------------
# Name:        La position de la fenêtre principale dans le bureau
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

root = Tk()
root.title("La position de la fenêtre principale dans le bureau")

cnv = Canvas(root, width=600, height=600, bg='ivory')
cnv.pack()

#root.update_idletasks()
"""
La ligne root.update_idletasks() est parfois nécessaire pour initialiser
certaines tâches (sinon, dans notre cas, le message est 1x1+0+0).
"""
#print(root.geometry())
"""
Chaine de Géometrie : WxH ± X ± Y
où W; H; X; Y désignent des mesures en pixels avec la signication suivante :

W   :   Largeur de la fenêtre
H   :   Hauteur de la fenêtre
X   :   Distance à l’un des deux bords verticaux du bureau.
        Bord gauche du bureau si signe +.
        Bord droit du bureau si signe -.
Y   :   Distance à l’un des deux bords horizontaux du bureau.
        Bord supérieur du bureau si signe +.
        Bord inférieur du bureau si signe -.

Exemple : 300x200-5+40
Cette chaîne donne les informations suivantes concernant la fenêtre générée :
— sa largeur est de 300 px,
— sa hauteur est de 200 px
— le bord droit de la fenêtre est à 5 px du bord droit du bureau,
— le bord supérieur de la fenêtre est à 40 px du haut du bureau
"""
root.geometry("+500+500")

root.mainloop()
