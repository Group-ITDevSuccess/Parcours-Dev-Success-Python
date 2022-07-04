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
from tkinter import ttk

root = Tk()
root.title("Progression arréter")

progress = ttk.Progressbar(root, maximum = 300, length=400)
progress.pack(pady=30)

unit = 10
progress.start(10)

def anim(value):
    #On surveille la variable value de la barre
    """
    Si la barre redémarre à zéro, c'est que la valeur courant de value diminue
    """
    if progress["value"] < value:
       """
       On arrête la barre de progression et pour qu'elle remplice la zone, value
       est affecté à la valeur de remplissage maximum
       """
       progress.stop()
       progress["value"] = progress["maximum"]
    #On redémare l'animation avec l'ancienne value
    root.after(unit, anim, progress["value"])

anim(0)

root.mainloop()