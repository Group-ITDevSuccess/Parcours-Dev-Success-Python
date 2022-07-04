#-------------------------------------------------------------------------------
# Name:        Evénement de la souris
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

root = Tk()
root.title("Evénement de la souris")
cnv = Canvas(root, width= 200, height=200)
cnv.pack(padx=10, pady=10)

#Création de rectangle gris:
cnv.create_rectangle(50,50,150,150, fill = 'gray')

#Pour la fonction clique
"""
La fonction clique, qand elle est automitiquement appelée suite à un clic gauche
dans le canevas, reçoit un argument représenté par le paramètre event traduisant
le clic de souris. Cet événement contient en attributs les coordonnées (event.x,
event.y) dans le canevas du clic de souris. Un simple calcul de savoir si le clic
est dans le rectangle ou à l'extérieur.
"""
def clique(event):
    if 50 < event.x < 150 and 50 < event.y < 150:
       print("INside")
    else:
         print("OUTside")

#Tout appui sur la bouton gauche de la sourie (événement <Button-1>):
"""
Entraine l'exécution de la fonction clique.
"""
cnv.bind("<Button-1>", clique)


root.mainloop()