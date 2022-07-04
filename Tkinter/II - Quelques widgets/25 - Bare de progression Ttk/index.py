#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     16/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, ttk
#Il faut impérativement importer ttk explicitement de tkinter
"""
Une importation de la forme  from tkinter import * ne donnera pas accès à Ttk
"""
root = Tk()
root.title("Mon bare de progression")

#Une barre de progression se crée comme tout autre widget :
"""
Construction et placement.

On peut définir la longeur de la barre avec l'option length.
"""
progress = ttk.Progressbar(root, length=400, maximum=300)
progress.pack(pady=30)

#Lancement de la progression dans la barre.Plus la valeur est grand et plus est lent
progress.start(10)

root.mainloop()