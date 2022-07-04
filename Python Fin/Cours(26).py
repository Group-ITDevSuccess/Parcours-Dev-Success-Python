#-------------------------------------------------------------------------------
# Name:        Le gestion du temps
# Purpose:  Cours 26
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
import time
"""
time.sleep(2)   : Metre en pose de 2 seconds le programme

# 1er Janvier 1970 à 00h00
print(time.time()) #TimeStamp

             localtime()
(TIMESTAMP) -------------> Structure de temps
            <-------------
              mktime()

time.sleep()
    .time()
    .localtime()
    .mktime()
    .strftime()
"""

"""
%d  : jour (01 à 31)
%m  : mois (01 à 12)
%Y  : année (ex : 2018) - %y (00 à 99)
%H  : heure (00 à 23)
%I  : minutes (00 à 59)
%S  : secondes (00 à 59)
%p  : AM/PM

%A  : Jours semaine / %a (jours abrégé)
%B  : mois / %b (mois abrégé)

%Z  : fuseau horaire (timezone)
"""
my_time = time.strftime("%Z")

print(my_time)