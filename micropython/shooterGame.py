from microbit import *
import radio
radio.on()
radio.config(channel = 2)
shooterX = 2
shooterY = 4
bulletX = 0
bulletY = 0
shooting = 0
acum = 0
shotAt = 0
missileY = -1
missileX = -1
while True:
    display.set_pixel(shooterX, shooterY, 9) #9 = luminozitate maxima 
    if shooting == 1:
        while bulletY > 0:
            display.set_pixel(bulletX, bulletY, 0)
            bulletY = bulletY - 1
            display.set_pixel(bulletX, bulletY, 9)
            display.set_pixel(shooterX, shooterY, 9) # afisare nava
            sleep(70)
        # de adaugat
        shooting = 0
        # radio sending value
        radio.send(str(bulletX))
        
    else:
        display.set_pixel(bulletX, bulletY, 0)
    
    if accelerometer.get_x() < -200 and running_time() - acum > 150 and shooting == 0:
        acum = running_time()
        display.set_pixel(shooterX, shooterY, 0) #0 = luminozitate minima
        shooterX = shooterX - 1
        if shooterX < 0:
            shooterX = 0
    elif accelerometer.get_x() > 200 and running_time() - acum > 150 and shooting == 0:
        acum = running_time()
        display.set_pixel(shooterX, shooterY, 0) #0 = luminozitate minima
        shooterX = shooterX + 1
        if shooterX > 4:
            shooterX = 4
    elif button_a.is_pressed() and shooting == 0:
        #sleep(100)
        if shooting == 0:
            bulletX = shooterX
            bulletY = shooterY
            shooting = 1
        # elif shooting == 1:
        #    display.set_pixel(bulletX, bulletY, 0) #sterg bullet
        #    bulletY = bulletY - 1
        #    if bulletY < 0:
        #        bulletY = 0
        #        shooting = 2
        
    coordonata = radio.receive()
    if coordonata != None:
        missileX = int(coordonata)
    if missileX in range(0, 5) and shotAt == 0:
        shotAt = 1
        display.set_pixel(missileX, 0, 5)
        missileY = 0
        acum = running_time()
    if shotAt == 1 and running_time() - acum > 50 and missileY < 4:
        acum = running_time()
        display.set_pixel(missileX, missileY, 0)
        missileY = missileY + 1
        display.set_pixel(missileX, missileY, 5)
    if missileY == 4:
        shotAt = 0
        if missileX == shooterX:
            display.clear()
            display.scroll("Lost")
        else:
            display.clear()
            display.set_pixel(shooterX, shooterY, 9)
        missileX = 10 #o valoare neutra pentru a nu relua desenarea obuzelor
    
