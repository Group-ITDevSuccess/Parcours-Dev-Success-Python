#-------------------------------------------------------------------------------
# Name:        Options d'un widget - lecture,écriture
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

root=Tk()
lbl =Label(root, text="Encore !", bg='pink', width=25)
lbl.pack(padx=50, pady=20)

#le label comme dictionnaire
print(lbl['text'])
#la méthode configure
print(lbl.configure('text'))
#la méthode cget dont le résultat est moins facilement interprétable
print(lbl.cget('text'))

root.mainloop()
