#-------------------------------------------------------------------------------
# Name:        Fenêtre non redimensionnable
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
root.title("Fenetre nonn redimmensionnable")

cnv = Canvas(root,width=400, height=400)
cnv.pack()

#Boquer le redimensionnement:
root.resizable(False, False)

root.mainloop()