#-------------------------------------------------------------------------------
# Name:        Modifier le profil de la flèche
# Purpose:
#
# Author:      Muriel
#
# Created:     20/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

root= Tk()
cnv = Canvas(root, width=200, height=200, bg='ivory')
cnv.pack()

cnv.create_line(50,60,150,60,width=8, arrow='last',arrowshape=(18,30,8))

#Voici la descrition de l'option arrowshape = (h, b, c)
"""
- h est la distance à l'axe de la flèche
- b est la largeur de la base de la flèche (la partie qui est sur l'axe)
- c est la longueur de la partie extérieure de la flèche
"""

root.mainloop()