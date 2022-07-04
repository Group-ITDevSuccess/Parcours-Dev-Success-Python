#-------------------------------------------------------------------------------
# Name:        PLacer des grille avec grid et pack
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

"""
La méthode pack n’est pas adaptée à présenter une interface
dont les widgets sont placés engrille
"""
from tkinter import *

root= Tk()

Canvas(root, bg="ivory").grid(row=0, column=0)
Scrollbar(root, orient="vertical").grid(row=0, column=1, rowspan=2,sticky=NS)
Scrollbar(root, orient="horizontal").grid(row=1, column=00,sticky=EW)



root.mainloop()