#-------------------------------------------------------------------------------
# Name:        Le widget spinbox
# Purpose:
#
# Author:      Muriel
#
# Created:     16/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *
root=Tk()
root.title("Le spinbox avec des zone de texte")

fruits = ["Litchie","Kiwi","Orange","Raisin","Citron","Cerise"]

sp = Spinbox(root,
   values=fruits,
   width=8, #L'option width est le nombre de caractères visibles dans la zone de texte
   bg="white", #bg est la couleur de fond
   justify=CENTER, #Justify permet de disposer le texte dans la zone
   wrap = True,
   font="times 30") # Police et la taille du texte
#wrap = True
"""
Par défaut, quand le défilement arrive en bout de succession, lle défilement est
bloqué. L'option wrap permet d'aller en une clic à l'aurte extrémité de le succession.
"""
sp.pack(padx=10, pady=10)

root.mainloop()