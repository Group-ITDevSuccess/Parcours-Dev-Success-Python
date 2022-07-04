#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     20/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Canvas, mainloop, Tk

def circle(canvas, x, y, r, width):
    return canvas.create_oval(x+r, y+r, x-r, y-r, width=width)

def circular_arc(canvas, x, y, r, t0, t1, width):
    return canvas.create_arc(x-r, y-r, x+r, y+r, start=t0, extent=t1-t0, style='arc', width=width)

def ellipse(canvas, x, y, r1, r2, width):
    return canvas.create_oval(x+r1, y+r2, x-r1, y-r2, width=width)

def elliptical_arc(canvas, x, y, r1, r2, t0, t1, width):
    return canvas.create_arc(x-r1, y-r2, x+r1, y+r2, start=t0, extent=t1-t0, style='arc', width=width)

def line(canvas, x1, y1, x2, y2, width, start_arrow=0, end_arrow=0):
    arrow_opts = start_arrow << 1 | end_arrow
    arrows = {0b10: 'first', 0b01: 'last', 0b11: 'both'}.get(arrow_opts, None)
    return canvas.create_line(x1, y1, x2, y2, width=width,arrow=arrows)

def text(canvas, x, y, text):
    return canvas.create_text(x, y, text=text, font=('bold', 20))
w = Canvas(Tk(), width=1000, height=600, bg='white')

circle(w, 150, 300, 70, 3) # q0 outer edge
circle(w, 150, 300, 50, 3) # q0 inner edge
circle(w, 370, 300, 70, 3) # q1
circle(w, 640, 300, 70, 3) # q2
circle(w, 910, 300, 70, 3) # q3
# Draw arc from circle q3 to q0.

midx, midy = (150+910) / 2, 300
r1, r2 = 910-midx, 70+70
elliptical_arc(w, midx, midy, r1, r2, 30, 180-30, 3)
line(w, 10, 300, 80, 300, 3, end_arrow=1)
line(w, 220, 300, 300, 300, 3, end_arrow=1)
line(w, 440, 300, 570, 300, 3, end_arrow=1)
line(w, 710, 300, 840, 300, 3, end_arrow=1)
text(w, 150, 300, 'q0')
text(w, 370, 300, 'q1')
text(w, 640, 300, 'q2')
text(w, 910, 300, 'q3')
w.pack()

mainloop()
