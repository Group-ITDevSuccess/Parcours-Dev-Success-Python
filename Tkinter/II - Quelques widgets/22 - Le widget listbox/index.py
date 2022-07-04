#-------------------------------------------------------------------------------
# Name:        Le widget listbox
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

#Liste des chaines qui vont apparaître dans le widget:
fruits = ["Litchie","Kiwi","Orange","Raisin","Citron","Cerise"]

n = len(fruits)

master = Tk()
master.title("Mon liste de sélection")

#Construction et placement du widget:
   #Certaine option de widget:
"""
- width est le nombre de caractères (pas de pixels)
- height est le nombre d'entrées devant apparaître dans la liste
- font : la police utilisée
- selectbackground : couleur du fond d'une cellule sélectionnée
"""
lbox = Listbox(
     master,
     width=8,
     height=n,
     font="Verdana 30 bold",
     selectbackground="lightblue")
lbox.pack(padx=50,pady=50)

#Insertion des éléments dans la liste du widget:
"""
END signifie qu'on place l'item courant après le dernier placé
"""
for item in fruits:
    lbox.insert(END, item)


master.mainloop()