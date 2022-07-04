#-------------------------------------------------------------------------------
# Name:        module1
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

def f(drn):
    print(drn)

root = Tk()

g = root.register(f)

fruits = ["Litchie","Kiwi","Orange","Raisin","Citron","Cerise"]

sp = Spinbox(
   root,
   values = fruits,
   width=8,
   justify=CENTER,
   wrap=True,
   font="times 30",
   state="readonly",
   readonlybackground="white",
   command =  (g, "%d")) #La commande est fournie sous forme de tuple
"""
Le prémier élément du tuple est le retour d'un appel à la fonction encapsulée
va recevoir(ici, un seul paramètre ). Ces tuples sont conventionnelement définis
par Tkinter. Icipar exemple, le type %d représente une chaîne de caractères valant
Up si la flèche haut à été pressée et down si c'est flèche bas.
"""
sp.pack(padx=10, pady=10)

root.mainloop()