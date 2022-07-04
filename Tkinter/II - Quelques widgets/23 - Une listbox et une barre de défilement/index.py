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
#Pour raison d'esthétique, j'ai choise d'utliser la barre de Ttk
from tkinter import ttk

fruits = ["Un","Deux","Trois","Quatre","Cinq","Six","Sept"] * 5

master = Tk()
master.title("Mon liste avec de scole")

lbox = Listbox(
     master,
     width=8,
     height= 5,
     font="Verdana 30 bold",
     selectbackground="#0f0fff")
lbox.pack(side= LEFT, padx = 40, pady=40)

for item in fruits:
    lbox.insert(END, item)
#On place une barre (par défaut verticale):
"""
Sa commande pointe vers le déplacement vertical (yview) de items de la liste lbox
"""
sbar = ttk.Scrollbar(master, command=lbox.yview)

#On place soigneusement la barre pour qu'elle recouvre toute la côté de la liste
sbar.pack(side = LEFT, expand= True, fill=Y)

#On apparie cette fois la listbox  à la barre
lbox.config(yscrollcommand=sbar.set)

master.mainloop()