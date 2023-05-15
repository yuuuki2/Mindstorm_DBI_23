import nxt.locator
import nxt.motor
import nxt.sensor
import nxt.sensor.generic


with nxt.locator.find() as b: 
    motor = b.get_motor(nxt.motor.Port.B) # Motor suchen (Port A) und der Variable zuweisen
    sensor = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.generic.Touch) # Sensor suchen (Port 1) und der Variable zuweisen
    us = b.get_sensor(nxt.sensor.Port.S4)
    
    while True:
        value = sensor.get_sample()
        if value == True:
            for i in range(29):
                motor.turn(24, 4) 
                print(us.get_sample())
                if i == 28:
                    for _ in range(29):
                        motor.turn(-24, 5) 
                        print(us.get_sample())
        else:
            print(us.get_sample())



