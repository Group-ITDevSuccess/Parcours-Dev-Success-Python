#-------------------------------------------------------------------------------
# Name:        Utilisation de gestionnaire de géometrie grid
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
root.title("Le gestionnaire de géométrie grid()")

cnv = Canvas(root, width = 400, height = 300, bg = "orange")
cnv.grid(row = 0, column = 0)

pomme = Button(root, text = "Pomme")
pomme.grid(row=1,column=0)

kiwi = Label(root, width = '10', text = 'Kiwi')
kiwi.grid(row = 2, column = 0)

begonia = Label(root, width = '10', text = 'Begonia')
begonia.grid(row = 1, column = 1)

#Les options de grid :
"""
OPTION      CARACTERISTIQUES        VALEURS POSSIBLES       VALEUR PAR DEFAUT

sticky:     Étirement du widget         Un ancre :              Center
            dans certaines directions   N, E, W, etc
            nord, sud, etc pour
            remplirplace restante
            dans la cellule

columnspan: Répartir sur plusieurs      Entier positif              1
            colonnes consécutives

rowspan:    Répartir sur plusieurs      Entier positif              1
            lignes consécutives

padx:       Marge horizontale           Entier positif              0
            (en pixels)

pady:       Marge vertivcale            Entier positif              0
            (en pixels)

"""

root.mainloop()