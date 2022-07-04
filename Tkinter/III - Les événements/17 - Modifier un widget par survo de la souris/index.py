#-------------------------------------------------------------------------------
# Name:        Modifier un widget par survo de la souris
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

root=Tk()
root.title("Modifier un widget par survo de la souris")
side =350
pad=30
cnv = Canvas(root, width=side, height=side)
cnv.pack(padx=100, pady=100)

def go_in(event):
    cnv['bg'] = "pink"

def go_out(event):
    cnv['bg'] = "royal blue"

cnv.bind("<Enter>", go_in)
cnv.bind("<Leave>", go_out)


root.mainloop()