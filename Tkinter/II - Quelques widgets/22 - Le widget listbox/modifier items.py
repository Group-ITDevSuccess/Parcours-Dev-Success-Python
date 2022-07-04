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

root = Tk()
MOIS = ['janvier','février','mars','avril','mai','juin','juillet','août',
       'septembre','octobre','novembre','décembre']

#Le texte de chaque ligne est initialement placé dans une variabmles dynamqie Tkinter
z = StringVar(value=MOIS)
lb = Listbox(root, width=16, fg='orange', listvar= z,
     selectbackground = 'pink', font ='Arial 16 bold')
lb.pack(side=LEFT, padx = 10, pady = 10)

def modif():
    for i in range(len(MOIS)):
        MOIS[i] = MOIS[i].upper()
    #La méthode set de la variabmle dynamique permet une mise à jour automatique
    z.set(MOIS)

#Au bout de 2,5 secondes après l'ouverture de la fenêtre, la case des lignes de la listbox est changée
root.after(2000, modif)

root.mainloop()