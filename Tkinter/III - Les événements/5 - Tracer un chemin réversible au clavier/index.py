#-------------------------------------------------------------------------------
# Name:        Tracer un chemin réversible au clavier
# Purpose:
#
# Author:      Muriel
#
# Created:     17/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

WIDTH = 400
HEIGHT = 200
COTE = 40

root = Tk()
root.title("Tracer un chemin réversible au clavier")
cnv = Canvas(root, width=WIDTH, height= HEIGHT, bg="ivory")
cnv.pack()

#Chaque appui sur une des flèches du clavier est associé à un décalage suivat le repère du canevas
"""
Par exemple, à un appui sur la flèche bas est associé la direction correspondante,
ici le coupe est (0,-1). C'est juste une facilité pour coder la fonction bouge.

"""
DIR = {'Left':(-1,0),'Right':(1,0),'Up':(0,-1),'Down':(0,1)}

def bouge(event):
    key = event.keysym
    dx, dy = DIR[key]
    a, b, segment = pile[-1]

    #La détection d'une marche arrièrer. le segment est affacé
    if len(pile) >=2  and a+dx == pile[-2][0] and b+dy ==pile[-2][1]:
       pile.pop()
       print("back")
       cnv.delete(segment)
    else:
         #Si pas de retour en arrière:
         """
         Le segment pour le nouveau déplacement est rendu visible et rajouté dans la pile
         """
         segment = cnv.create_line(a*COTE+COTE//2, b*COTE+COTE//2,
                                   a*COTE+COTE//2+dx*COTE,
                                   b*COTE+COTE//2+dy*COTE,
                                   fill="lightblue", width=4, capstyle = ROUND)
         pile.append([a+dx, b+dy, segment])
    #La sortie du canevas n'est pas gérée par le programme.
    cnv.move("perso", dx*COTE, dy*COTE)

#Un carré bleu indique la position courant sur le canevas:
perso = cnv.create_rectangle(0,0,COTE, COTE, fill="blue",
      outline='',tag='perso')

#Les différents mouvements de l'utlisateur sont enregistrés dans une pile
"""
La pile permet (en déplant) de revenir en arrière et d'effacer le trajet de retour.

"""
pile = [(0,0, perso)]

#L'appui sur une des 4 flèches du clavier est détecté par le canevas:
for key in ["<Left>","<Right>","<Up>","<Down>"]:

#Le canevas a le focus car la fenêtre entier (root) a le focus quand l'application est lancée
    #Tout appui sur une des touches du clavier exécute la fonction bouge
    root.bind(key, bouge)

root.mainloop()