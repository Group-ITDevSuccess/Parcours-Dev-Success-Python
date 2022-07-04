#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     15/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

#On crée, en respectant l'ordre, une liste des couleurs associées aux différentes fruits
fruits = fruits = ["Litchie","Kiwi","Orange","Raisin","Citron","Cerise"]
couleurs = ["pink","lightgreen","orange","purple","yellow","red"]
n = len(fruits)

master = Tk()

lbox = Listbox(
     master,
     width=8,
     height=n,
     font="Arial 20 bold",
     selectbackground="lightblue")
lbox.pack(padx=20, pady=20, side=LEFT)

for item in fruits:
    lbox.insert(END, item)

lbox.focus_set()
pos = 1
lbox.activate(pos)
lbox.selection_set(pos)

for i in range(0, len(fruits), 2):
    lbox.itemconfigure(i, background='#f0f0ff')
for i in range(1, len(fruits), 2):
    lbox.itemconfigure(i, background='#ffffff')

def show(event):
    #Rappel : début à l'index 0
    """
    La méthode curselection de Listbox permet de récupérer l'index de la cellule
    séléctionnée.
    """
    index = lbox.curselection()[0]
    cnv["bg"] = couleurs[index]

#Le point essentiel:
"""
L'événement virtuel <<ListboxSelect>> qui réagit chaque foins qu'une cellule est
sélectionnée en appelant une fonction, ici la fonction show qui vas placer la
la bonne couleur sur le canevas.
"""
lbox.bind('<<ListboxSelect>>', show)

#On crée un canevas qui va afficher la couleur de l'élement sélectionné
cnv = Canvas(master, width=200,height=200, bg='ivory')
cnv.pack(padx=5, pady=5,side=RIGHT)
cnv["bg"] = couleurs[pos]

master.mainloop()