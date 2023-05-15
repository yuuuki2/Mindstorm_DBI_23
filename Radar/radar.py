import nxt.locator
import nxt.motor
import nxt.sensor
import nxt.sensor.generic

with nxt.locator.find() as b: # 
    motor = b.get_motor(nxt.motor.Port.B) # Motor suchen (Port A) und der Variable zuweisen
    sensor = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.generic.Touch) # Sensor suchen (Port 1) und der Variable zuweisen
    us = b.get_sensor(nxt.sensor.Port.S4)
    
    while True:
        try:
            value = sensor.get_sample()# Wert des Sensors der Variable value zuweisen
            if value == True:
                motor.turn(20, 180) # Motor Drehen um 180 Grad mit geschw. 64
                motor.turn(-20,180)


        except: # Fehlermeldung abfangen und ignorieren wenn value == False
            pass
