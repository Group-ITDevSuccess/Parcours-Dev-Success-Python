#-------------------------------------------------------------------------------
# Name:        Les boutonq radion
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

root = Tk()
root.title("Mon bouton radion")

pad = 30

def colorer():
    val = fruit.get()
    if val =="cerise":
       lbl_fruit["bg"] = "red"
    elif val == "orange":
         lbl_fruit["bg"] = "orange"
    else:
         lbl_fruit["bg"] = "yellow"

fruit = StringVar()
fruit.set("cerise")

cerise = Radiobutton(
       root,
       text="Cerise",
       variable=fruit,
       value="cerise",
       font="Arial 20")
cerise.pack(anchor="w")

orange = Radiobutton(root,
       text="Orange",
       variable=fruit,
       value="orange",
       font="Arial 20")
orange.pack(anchor="w")

banane = Radiobutton(root,
       text="Banane",
       variable=fruit,
       value="banane",
       font="Arial 20")
banane.pack(anchor="w")

lbl_fruit = Label(root, bg="white",width=10)
lbl_fruit.pack(padx=50,pady=30)

btn = Button(root, text = "Couleur",command=colorer)
btn.pack(padx=50,pady=0)

root.mainloop()