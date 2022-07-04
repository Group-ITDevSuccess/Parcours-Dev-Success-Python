#-------------------------------------------------------------------------------
# Name:        Déplacement amélioré avec deux touches (Windows)
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

WIDTH = 800
HEIGHT= 500

root = Tk()
root.title("Déplacement amélioré avec deux touches (Windows)")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="ivory")
cnv.pack(pady=10, padx=10)
cnv.focus_set()

SIDE = 30
UNIT = 2

rect = cnv.create_rectangle(
    (WIDTH /2 - SIDE / 2, HEIGHT / 2 - SIDE / 2),
    (WIDTH /2 + SIDE / 2, HEIGHT / 2 + SIDE / 2),
    fill="black")

def handler():
    unit = UNIT
#Poure sum
    """"
    Si deux touches son ppressées simultanément, la vitesse du déplacement est
    rectifiée pour qu'elle correspondre à peu près au déplacement horizontal ou
    vertical.
    """
    if sum(keys.values()) > 1:
       unit = UNIT / 1.5

    for key in drn:
#Si la touche est active (elle est pressée), le mouvenemt correspondant est exécuté
        if keys[key]:
           if key == "Up":
              cnv.move(rect, 0, -unit)
           elif key == "Right":
                cnv.move(rect, unit, 0)
           elif key == "Left":
                cnv.move(rect, -unit, 0)
           elif key == "Down":
                cnv.move(rect, 0, unit)
    #Toutes les 20 ms, la fonction handler est appelée.
    """
    Elle examine l'état de chacune des 4 touches.
    """
    root.after(20, handler)

#Poure les deux fonction:
"""
Les états son enregistrés par les fonctions press et release qui sont appelées
automatiquement par Tkinter après liaison.
"""
def press(event):
    keys[event.keysym] = True

def release(event):
    keys[event.keysym] = False
#L'état de chacuune des 4 flèches du clavier est enregistré dans le dictionnaire keys
"""
Pour chacune des flèches, on enregistre si elle est activée ou pas.
"""
drn = ["Up","Right","Left","Down"]
keys = dict.fromkeys(drn, False)

for key in drn:
    cnv.bind("<KeyPress-%s>" %key, press)
    cnv.bind("<KeyRelease-%s>" %key, release)

handler()

root.mainloop()