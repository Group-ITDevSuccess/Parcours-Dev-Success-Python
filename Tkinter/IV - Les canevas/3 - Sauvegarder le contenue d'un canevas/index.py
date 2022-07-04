#-------------------------------------------------------------------------------
# Name:        Sauvegarder le contenu du canevas
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

SIDE = 300
SEP = 50

def print_cnv():
    #La méthode postscript du canevass permet d'exporter au format esp
    """
    On désigne un fichier avec l'argument nommé file.
    """
    cnv.postscript(file="sauve.eps",colormode='color')

master = Tk()
master.title("Sauvegarder le contenu du canevas")

cnv = Canvas(master, width=SIDE, height=SIDE, bg='lavender')
cnv.pack(pady=10, padx=10)

#On peut capturer les items de Tkinter
"""
Comme des rectangles ou du texte. La capture d'image Photoimage ne fonctionne pas.
"""
cnv.create_rectangle(SEP, SEP, SIDE-SEP, SIDE-SEP, fill="gray")
cnv.create_text(SIDE/2, SIDE/2, text="Salam Alaikum\nMuriel",
                        fill ="white", font='Times 20 bold', justify=CENTER)

#Il faut attendre que le canevas soit dessiné
cnv.after(1000, print_cnv)

master.mainloop()