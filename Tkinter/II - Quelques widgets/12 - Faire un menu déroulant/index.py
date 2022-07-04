#-------------------------------------------------------------------------------
# Name:        Ménue déroulant
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

root = Tk()
root.title("Mon Menu déroulant")

cnv =Canvas(root, width=400, height=400, bg='lavender')
cnv.pack()

def rose():
    cnv['bg'] ='pink'

def rouge():
    cnv['bg'] ='red'

def orange():
    cnv['bg'] ='orange'

def violet():
    cnv['bg'] ='purple'

#Barre de menus
mon_menu = Menu(root)
root.config(menu=mon_menu)

#Menu légumes
legumes = Menu(mon_menu, tearoff=0)
legumes.add_command(label="Radis",command=rose)
legumes.add_separator()
legumes.add_command(label="Tomates",command=rouge)
mon_menu.add_cascade(label="Légumes", menu = legumes )

#Menu fruits
fruits = Menu(mon_menu,tearoff=0)
fruits.add_command(label="Raisin", command=violet)
fruits.add_command(label="Orange", command=orange)
mon_menu.add_cascade(label="Fruits", menu=fruits)

root.mainloop()