# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 06:08:11 2022
@name: Calcule du prochaine vendredi 13
@author: Muriel
"""

from datetime import date

def prochaine13(x):
    m = x.month
    d = x.day
    y = x.year
    if d < 13:
        return date(y, m, 13)
    else:
        if m < 12:
            return date(y, m +1,13)
        else:
            return date(y+1, 1, 13)
    
x = date.today()

while True:
    x = prochaine13(x)
    if x.weekday() == 4:
        print('Vendrerdi 13/%d/%d' %(x.month, x.year))        
        break