import nxt.locator
import nxt.motor
import nxt.sensor
import nxt.sensor.generic
import time

x = False

with nxt.locator.find() as b:
    motor_a = b.get_motor(nxt.motor.Port.A)
    motor_b = b.get_motor(nxt.motor.Port.B)
    sensor = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.generic.Touch)

    while True:
        value = sensor.get_sample()
        if value == False: 
            x = True
            motor_a.run(-70, True)
            motor_b.run(-70, True)
        if value == True:
            if x == True:
                motor_a.run(-70, True)
                motor_b.run(70, True)
                time.sleep(3)
                x == False

