#-------------------------------------------------------------------------------
# Name:        Opération avec python
# Purpose:      Cours 4
#
# Author:      Muriel
#
# Created:     01/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

"""
Opérateur en Python :   + (addition)
                        - (soustraction)
                        * (multiplication)
                        / (division)
                        % (modulo) -> reste d'une division Euclidienne

"""
calcule = 5 / 2
rest = 5/2
calcule = int(calcule)
rest = float(rest)

print("Le calcule est {} et le reste est {}".format(calcule,rest))

niveau = 1
print("Niveau de depart", niveau)
# niveau = niveau + 1 <=> niveau += 1
niveau += 1
print("Niveau de versonnage", niveau)


