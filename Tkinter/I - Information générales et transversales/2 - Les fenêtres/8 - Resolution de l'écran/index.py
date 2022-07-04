#-------------------------------------------------------------------------------
# Name:        Résolution de l'écran
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

root = Tk()
root.title("Résolution de l'écran")
cnv = Canvas(root, width = 400, height=400)
cnv.pack()

#Récupérer les informations de la résolution de l'écran
print(root.winfo_screenwidth(), root.winfo_screenheight())

root.mainloop()