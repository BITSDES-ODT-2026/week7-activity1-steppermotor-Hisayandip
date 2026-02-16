from machine import Pin


import time 



motor1 = Pin(5, Pin.OUT)
motor2 = Pin(18, Pin.OUT)
motor3 = Pin(19, Pin.OUT)
motor4 = Pin(21, Pin.OUT)
while True:
    
    motor1.on()
    motor2.off()
    motor3.off()
    motor4.off()
    time.sleep(0.005)

    motor1.on()
    motor2.on()
    motor3.off()
    motor4.off()
    time.sleep(0.005)

    motor1.off()
    motor2.on()
    motor3.off()
    motor4.off()
    time.sleep(0.005)

    motor1.off()
    motor2.on()
    motor3.on()
    motor4.off()
    time.sleep(0.005)
    
    motor1.off()
    motor2.off()
    motor3.on()
    motor4.off()
    time.sleep(0.005)

    motor1.off()
    motor2.off()
    motor3.on()
    motor4.on()
    time.sleep(0.005)

    motor1.off()
    motor2.off()
    motor3.off()
    motor4.on()
    time.sleep(0.005)

    motor1.on()
    motor2.off()
    motor3.off()
    motor4.on()
    time.sleep(0.005)
    

