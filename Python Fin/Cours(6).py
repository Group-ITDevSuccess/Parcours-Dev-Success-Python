#-------------------------------------------------------------------------------
# Name:        Les Boucles
# Purpose:      Cours 6
#
# Author:      Muriel
#
# Created:     01/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

"""
Boucle  : while / for
Mots-clés:  break (casse la boucle) / continue (revient au début de la boucle)

"""
compteur = 0

while (compteur < 2):
    print("je suis une Phrase")
    compteur += 1

jeuLance = True

while jeuLance:
    choixMenu = input("> ")

    if choixMenu == "again":
        continue
    elif choixMenu == "quit":
        break
    elif choixMenu == "hello":
        print ("Bonjour :) !")
    else:
        print("Commande introuvable")

sentence = "Salam Alaikum :) !"

for letter in sentence:
    print(letter)

print("A bientôt...")


