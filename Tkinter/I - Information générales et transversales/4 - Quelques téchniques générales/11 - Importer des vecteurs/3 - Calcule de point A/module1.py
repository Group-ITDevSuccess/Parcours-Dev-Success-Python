#-------------------------------------------------------------------------------
# Name:        Caclue de point de B
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from turtle import Vec2D

A = (5, 2)
C = (-1, 5)

A = Vec2D(*A)
C = Vec2D(*C)
AC = C - A

u = 1/abs(AC)*AC
print(u)

lg = 3
B = A + lg*u

print(B)


