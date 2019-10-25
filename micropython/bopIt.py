# Add your Python code here. E.g.
from microbit import *
from random import randint

def showA():
    display.clear()
    display.show('A')
    
def showB():
    display.clear()
    display.show('B')

pauza = 1000
nivel = 1
scor = 0
rezultat = False
gameOn = True
startTime = running_time()

def getAction():
    global optiune
    r = False
    startTime = running_time()
    while running_time() - startTime < pauza:
        if (button_a.is_pressed() and optiune == 1) or (button_b.is_pressed() and optiune == 0):
            r = True
            break
        elif (button_a.is_pressed() and  optiune == 0) or (button_b.is_pressed() and optiune == 1):
            r = False
            break
    return r


while True:
    while gameOn:
        optiune = randint(0,1)
        if optiune == 1:
            showA()
            rezultat = getAction()
        else:
            showB()
            rezultat = getAction()
        
        if rezultat:
            display.show('k')
            scor += 10
            nivel += 1
            pauza -= 100
        else:
            display.show('n')
            gameOn = False
        sleep(300)
    
    display.scroll('scor: ')
    display.scroll(scor)
    sleep(1000)
