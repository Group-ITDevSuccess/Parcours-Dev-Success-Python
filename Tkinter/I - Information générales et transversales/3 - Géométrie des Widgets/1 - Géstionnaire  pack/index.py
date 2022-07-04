#-------------------------------------------------------------------------------
# Name:        Utilisation de gestionnaire de géometrie pack
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
root.title("Le géstionnaire de géométrie pack()")

cnv = Canvas(root, width = 400, height=300, bg="orange")
cnv.pack()

bouton = Button(root, text="Pomme")
bouton.pack()

entree = Label(root, width='10', text="Kiwi")
entree.pack()

#Les options de pack :
"""
OPTION      CARACTERISTIQUES        VALEURS POSSIBLES       VALEUR PAR DEFAUT

side:       Le côté de la           TOP, BOTTOM,            TOP
            zone restante sur       RIGHT, LEFT
            lequel le widget
            va s’appuyer

fill:       Remplissage             X, Y, BOTH, NONE        NONE
            vertical ou
            horizontal

expand:     Expansion verticale     True, False             False
            ou horizontale dans la
            **fenêtre maîtresse**

anchor:     Ancrage du widget dans  9 ancres possibles :    CENTER
            l’espace qui lui reste  CENTER, N, NE, E, etc

padx:       Marge (en pixels)       entier positif          0
            horizontale à l’
            extérieur et de part
            et d’autre du widget

pady:       Marge (en pixels)       entier positif          0
            verticale à l’
            extérieur et de part
            et d’autre du widget
"""
root.mainloop()