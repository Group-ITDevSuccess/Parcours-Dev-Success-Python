#-------------------------------------------------------------------------------
# Name:        Cacher la fenêtre maintrese
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

def quit_a():
    a.destroy()
    if closed[1]:
        root.destroy()
    else:
        closed[0] = True
def quit_b():
    b.destroy()
    if closed[0]:
        root.destroy()
    else:
        closed[1] = True


root = Tk()
a = Toplevel(root, bg = 'red')
a.title("Mon Fentre Rouge")

b = Toplevel(root, bg = 'blue')
b.title("Mon Fentre Bleu")

a.protocol("WM_DELETE_WINDOW", quit_a)
b.protocol("WM_DELETE_WINDOW", quit_b)

closed = [False, False]

#Pour cacher la fenêtre maîtresse, utiliser withdraw :
root.withdraw()

root.mainloop()