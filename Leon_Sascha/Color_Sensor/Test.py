import nxt.sensor
import nxt.sensor.hitechnic
import nxt.locator
import nxt.motor
import time

with nxt.locator.find() as b:
    motor_left = b.get_motor(nxt.motor.Port.B)
    motor_right = b.get_motor(nxt.motor.Port.A)
    color = b.get_sensor(nxt.sensor.Port.S3, nxt.sensor.hitechnic.Colorv2)
    
    
    while True:
        red = color.get_active_color().red
        green = color.get_active_color().green
        blue = color.get_active_color().blue
        white = color.get_active_color().white
        
        print(color.get_active_color().red,color.get_active_color().green,color.get_active_color().blue, color.get_active_color().white)
        if red > green and red > blue and red > white: # kontroliert ob es rot ist
            motor_left.run(-70, True)
            motor_right.run(-70,True)
        
        
            
        else:
            motor_left.idle()
            motor_right.idle()           
        