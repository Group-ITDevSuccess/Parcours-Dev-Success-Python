#-------------------------------------------------------------------------------
# Name:        Titre de fenêtre
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Label

racine = Tk()
#Création de titre de la fenêtre:
racine.title("Mon Fenêtre avec un titre")

annonce = Label(height=5, width=50, text="Salam Alaikum", bg='ivory')
annonce.pack()

racine.mainloop()