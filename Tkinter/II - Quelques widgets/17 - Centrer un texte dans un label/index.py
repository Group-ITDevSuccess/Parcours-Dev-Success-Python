#-------------------------------------------------------------------------------
# Name:        Centrer un texte dans un label
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Label, CENTER

racine = Tk()

mon_texte= """
Salam Alaikum Muriel,
que Allah te bénise
et te donne la santé, le bonheur
et le paradis
"""
annonce = Label(height = 5,width= 50, text = mon_texte, justify = CENTER, bg='ivory')
annonce.pack()

racine.mainloop()