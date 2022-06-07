#-------------------------------------------------------------------------------
# Name:        Structure conditionnel
# Purpose:      Cours 5
#
# Author:      Muriel
#
# Created:     01/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

"""
Opérateur de comparaison :  == (égal à)
                            != (différent de )
                            < (plus petit que)
                            > (plus grand que=
                            <= (plus petit ou égal à)
                            >= (plus grand ou égal à)

Opérateur multiples:    and (ET)
                        or (OU)
                        in / not / not in (DANS / NON / PAS DANS)

Mots clés des conditions :  if / elif / else

"""

identifiant = "Muriel"
mot_de_passe = "muriel123"

print("Interface de connexion")

user_id = input("Entrez votre identifiant: ")
user_password = input("Entrez votre mot de Passe : ")

if (user_password == mot_de_passe) and (user_id == identifiant):
    print("Vous êtes connectés, bienvenue", user_id)

lettre_hasard = "q"

if lettre_hasard in "azerty":
    print ("C'est une clavier azerty")
else:
    print ("C'est une clavier qwerty")

jeu_charge = True #True = vrai (=1)

if jeu_charge:
    print("Le jeu est chargé")

age = input("Votre age : ")
age = int(age)

#age > 0 ET age <= 100  <=>  0 < age <= 100

if 0 < age <= 100:
    print("L'age est valide")
else:
    print("L'age est invalide")