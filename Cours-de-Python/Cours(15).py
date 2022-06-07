#-------------------------------------------------------------------------------
# Name:        Les Chaines de Caractères
# Purpose:  Cours 15
#
# Author:      Muriel
#
# Created:     05/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
"""
Une méthode de chaine travaille sur une copie,
et pas sur la chaine
str.upper(), str.lower(), str.capitalize(),
str.title(), str.center(<largeur>, <caractere_remplissage>)
str.find(<chaine>, <debut>, <fin>)
str.index(<chaine>,<debut>,<fin>)
str.replace(<anienne>,<nouvelle>, <occurence>)

str.isalpha(), str.isdigit(), str.isdecimal(),
str.isnumeric(), str.isalphanum()

str.islower(), str.isupper()

str.isidentifer(), str.iskeyword()
"""


ma_chaine = "Salam Alaikum Muriel"

try:
    print(ma_chaine.index("Musriel"))

except ValueError:
    print("Chaine non pas trouver")