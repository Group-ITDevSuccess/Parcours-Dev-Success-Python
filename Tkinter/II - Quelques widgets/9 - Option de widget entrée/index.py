# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 11:37:56 2022

@author: Muriel
"""
# coding:utf-8

from tkinter import *
root = Tk()
root.title("Mon entrer personnaliser")
my_entry = Entry(root,
                 font='Arial 60 bold',
                 width='5',
                 bg='lavender',
                 insertofftime=500,
                 insertbackground='red',
                 relief=FLAT)
my_entry.pack(padx=20, pady=20)

# On peut forcer l'acquisition du focus par la méthode focus_set :
my_entry.focus_get()
# =============================================================================
# Donc, dès que l’application s’ouvre, l’entrée est réceptive aux touches de clavier
# Quand le focus est actif, un curseur guide la saisie
# Le clignotement du curseur est modifable avec l’option insertofftime qui désigne la durée en millisecondes
# (si 0 alors aucun clignotement).
# La couleur du curseur est contrôlée par l'option insertbackground
# Le style de relief de l’entrée est contrôlé par l’option relief, par défaut, on a relief=SUNKEN
# =============================================================================

root.mainloop()
