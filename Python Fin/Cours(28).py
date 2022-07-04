#-------------------------------------------------------------------------------
# Name:        La porgrammation asynchrone
# Purpose:  Cours 28
#
# Author:      Muriel
#
# Created:     11/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
import time
import threading

#Creation de véroue:
my_lock = threading.RLock()

#Mon classe:

class MyProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        while i< 3:
            """
            print(threading.current_thread()) #Envoyer l'information du thread
            time.sleep(0.3)
            """
            with my_lock: #Mise en place du véroue
                letters= "ABC"
                for lt in letters:
                    print(lt)
                    time.sleep(0.3)
            i += 1

th1 = MyProcess()
th2 = MyProcess()

    #On les démare:
th1.start()
th2.start()
    #On arret:
th1.join()
th2.join()

# Programation Séquenciel:
"""
def process_one():
    i = 0
    while i< 3:
        print("oooooooooooo")
        time.sleep(0.3)
        i += 1

def process_two():
    i = 0
    while i< 3:
        print("xxxxxxxxxxxxx")
        time.sleep(0.3)
        i += 1
"""
#Affichage de la fonction
"""
process_one()
process_two()
"""
#Porgrammation asynchrone:
"""
#Utlisation de thread

th1 = threading.Thread(target=process_one)
th2 = threading.Thread(target=process_two)
    #On les démare:
th1.start()
th2.start()
    #On arret:
th1.join()
th2.join()
"""
print("Fin de programme")