#-------------------------------------------------------------------------------
# Name:        Créer et intégrer une widget en une seule instruction
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *

root = Tk()
lbl = Label(root, text = "Salam Alaikum !", font='Arial 30 bold')
lbl.pack(padx =15, pady=15)

print(lbl["text"])

root.mainloop()
