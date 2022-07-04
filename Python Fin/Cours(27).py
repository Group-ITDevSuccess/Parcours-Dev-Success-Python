#-------------------------------------------------------------------------------
# Name:        La gestion des dates
# Purpose:  Cours 27
#
# Author:      Muriel
#
# Created:     11/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

import datetime

d1 = datetime.datetime(2022, 9, 18, 9, 36,42)
#ou même chose : d1 = datetime.date(2022, 9, 18, 9, 36,42)
#print(d1)
d2 = datetime.datetime(2001, 9, 18, 9, 36,42)

t1 = datetime.time(23, 00,00)
if(d1 < d2):
    print("Vous n'êtes pas encore né")
elif(d1 == d2):
    print("Meme date")
else:
    print("Vous êtes déja né")

print(d1.year)
print(d1.day)
print(d1.hour)
print(d1.fold)
print(d1.tzinfo)

print(t1)

#Pour aficher la date actuel:
"""

from datetime import datetime

print(datetime.now())
        ou
from datetime import date
now = date.today()
print(now)

"""