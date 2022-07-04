#-------------------------------------------------------------------------------
# Name:       Utilisation d'une variable de contrôle dans un label
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

def plus():
    cpt.set(int(cpt.get())+1)

def moin():
    cpt.set(int(cpt.get())-1)

def initial():
    cpt.set('0')

root = Tk()
root.title("Utilisation d'une variable de contrôle dans un label")

cpt= StringVar()
cpt.set('0')

Label(root, text="Incrémenter et Décrémenter \nUn Nombre", font="Times 20 bold").pack(padx=0,pady=10)

lbl = Label(root, width='10', textvariable = cpt, font='Arial 20 bold')
lbl.pack(side = TOP,padx=50,pady=10)

bouton = Button(root, text="+",command=plus)
bouton.pack(side = LEFT, padx=50, pady=10)

bouton = Button(root, text="Initialiser",command=initial)
bouton.pack(side = LEFT, padx=50, pady=10)

bouton = Button(root, text="-",command=moin)
bouton.pack(side = RIGHT, padx=50, pady=10)


root.mainloop()