#-------------------------------------------------------------------------------
# Name:        Dessiner un cercle, un disque
# Purpose:
#
# Author:      Muriel
#
# Created:     19/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
from tkinter import Tk, Canvas
SIDE = 500

root =Tk()
root.title("Mon cercle")
cnv = Canvas(root, width=SIDE, height=SIDE//1.5, bg="ivory")
cnv.pack(pady=10,padx=10)

da = 400
db = 180
#Le coté du carré et le diamètre du cercle ont même longueur
A = (a,b) = (50,80)
B = (a+da,b+db)

cnv.create_oval(A, B, fill='light blue', outline='red',width=2)

root.mainloop()