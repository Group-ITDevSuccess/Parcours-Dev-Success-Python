#-------------------------------------------------------------------------------
# Name:        Générer un code
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from random import randrange

COLORS=["red","blue","gray","orange","brown",
        "magenta","green","salmon","ivory",
        "cyan",'sky blue', 'light sky blue']

DIR=["RIGHT","LEFT","TOP","BOTTOM"]

cnv="""\
Label(fen,
        text='%s',
        font='Arial 10 bold',
        bg='%s', justify=LEFT).pack(
        side=%s, padx=%s, pady=%s, fill=%s,
        anchor='%s', expand=%s)
"""

FILL=["NONE","NONE","BOTH","X","Y"]
ANCHOR="NW N NE E SE S SW W CENTER".lower().split()
JUSTIFY="LEFT CENTER RIGHT".split()
EXPAND="0 1".split()

L=[]

for i in range(30):
    b= COLORS[randrange(len(COLORS))]
    c= DIR[randrange(4)]
    d= FILL[randrange(len(FILL))]
    e= ANCHOR[randrange(len(ANCHOR))]
    f= "%s" %JUSTIFY[randrange(len(JUSTIFY))]
    x=EXPAND[randrange(2)]

    padx=randrange(2,12)
    pady=randrange(2,6)
    options=(r"order=%s\ndir=%s\nfill=%s\n"\
            r"anchor=%s\nexpand=%s\npadx=%s pady=%s")
    a= options%(i+1, c, d, e, x, padx,pady)
    L.append(cnv %(a,b,c, padx, pady, d, e, x))

code= ["from tkinter import *"]

for i in range(1,15):


    code.append("# Fenêtre n°%s" %i)
    code.append("fen = Tk()\n")
    code.append("\n".join(L[:i]))
    code.append("#-----------------------------------\n\n")

code.append("fen.mainloop()")

open("mon_code.py","w").write('\n'.join(code))
