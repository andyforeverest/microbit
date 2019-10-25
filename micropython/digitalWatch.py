# Add your Python code here. E.g.
from microbit import *
import math

minut = 30
ora = 11
secunda = 20
timpScurs = 0
apasat_a = False
apasat_b = False

def increaseHour():
    global ora
    global apasat_a
    for i in range(0, 5):
        display.set_pixel(0, i, 0) #stingere leduri
    ora += 1
    if ora == 13:
        ora = 1

def increaseMinute():
    global minut
    global apasat_b
    for i in range(0, 5):
        display.set_pixel(1, i, 0) #stingere leduri
        display.set_pixel(2, i, 0) #stingere leduri
    minut += 1
    if minut == 60:
        minut = 0

def showHour(unitate, locatie):
    h = unitate
    hourLed = 4
    while h > 0:
        if h % 2 == 0:
            display.set_pixel(locatie, hourLed, 0)
        else:
            display.set_pixel(locatie, hourLed, 9)
        hourLed -= 1
        h = math.floor(h/2)
    

while True:
    m_units = minut % 10
    m_tens = (minut - m_units)/10
    s_units = secunda % 10
    s_tens = (secunda - s_units)/10
    
    if button_a.was_pressed() and apasat_a == False:
        increaseHour()
        apasat_a = True
    if button_b.was_pressed() and apasat_b == False:
        increaseMinute()
        apasat_b = True
    if running_time() - timpScurs > 1000:
        timpScurs = running_time()
        apasat_a = False
        apasat_b = False
        secunda += 1
        for i in range (0, 5):
            display.set_pixel(4, i, 0)
            display.set_pixel(3, i, 0)
        
        
        if secunda > 59:
            secunda = 0
            minut += 1
            for i in range (0, 5):
                display.set_pixel(1, i, 0) #stingere leduri
                display.set_pixel(2, i, 0)
            
            if minut > 59:
                minut = 0
                ora += 1
                for i in range (0, 5):
                    display.set_pixel(0, i, 0)
                
                if ora > 12:
                    ora = 1
    
    showHour(ora, 0)
    showHour(m_tens, 1)
    showHour(m_units, 2)
    showHour(s_tens, 3)
    showHour(s_units, 4)
   
    

