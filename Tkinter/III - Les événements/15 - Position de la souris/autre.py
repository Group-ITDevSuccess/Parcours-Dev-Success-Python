#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def _substitute(self, *args):

    getint = self.tk.getint
    def getint_event(s):
        try:
            return getint(s)
        except (ValueError, TclError):
               return s

    e.x = getint_event(x)
    e.y = getint_event(y)