#-------------------------------------------------------------------------------
# Name:        Le widget entrée
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

root = Tk()
root.title("Mon entrer")

my_entry = Entry(root)
my_entry.pack()

def affiche():
    """
    Une entrée Tkinter a une la méthode get qui permet de récupérer le contenu de
    l’entrée. Ici, ce contenu est affiché dans la console avec la fonction print.
    """
    print(my_entry.get())

buton = Button(root, text="Afficher",command=affiche)
buton.pack(padx=50, pady=10)


root.mainloop()