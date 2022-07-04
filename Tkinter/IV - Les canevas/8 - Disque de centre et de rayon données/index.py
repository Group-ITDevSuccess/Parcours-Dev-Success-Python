#-------------------------------------------------------------------------------
# Name:        Disque de centre et de rayon données
# Purpose:
#
# Author:      Muriel
#
# Created:     19/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

def dot(cnv, C, R=6, color='red', out='blue'):
    #Si le centre du cercle est C = (xC, yC) et que son rayon est R
    """
    C'est que le sommet A en haut à gauche extérieur au cercle est A = (xC-R,yC-R)
    et de même, le sommet B en bas à droite est B = (xC+R, yC+R)

    """
    xC, yC = C
    A = (xC - R, yC - R)
    B = (xC + R, yC + R)
    return cnv.create_oval(A, B, fill = color, outline=out)
#DIM sera le diamètre du disque, PAD est une marge pour le disque ne soit pas collé au bord du cnv
PAD = 50
DIM = 200
WIDTH = DIM + PAD
HEIGHT = DIM + PAD

root = Tk()
root.title("Mon fonction pour créer un cercle !")
cnv = Canvas(root, width= WIDTH, height=HEIGHT, bg='ivory')
cnv.pack()

#Les coordonnées du centre choisi. On a centré le point dans le canevas
C = (WIDTH // 2, HEIGHT // 2)

#Dessin d'un disque
dot(cnv, C, R = DIM//2, color = "pink",out="green")

root.mainloop()