import nxt.sensor
import nxt.sensor.hitechnic
import nxt.locator
import nxt.motor
import time


with nxt.locator.find() as b: #sucht die Motren und sensoren wenn vorhanden
    motor_left = b.get_motor(nxt.motor.Port.A) # Motor suchen (Port B) und der Variable zuweisen
    motor_right = b.get_motor(nxt.motor.Port.B)#
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
            for i in range(5):
                motor_left.run(-70)
                motor_right.run(70)
                time.sleep(2)
                motor_left.idle()
                motor_right.idle()
                
                red = color.get_active_color().red
                green = color.get_active_color().green
                blue = color.get_active_color().blue
                white = color.get_active_color().white
                
                if red > green and red > blue and red > white: # kontroliert ob es rot ist
                    break
                
                motor_left.run(70)
                motor_right.run(-70)
                time.sleep(2)
                motor_left.idle()
                motor_right.idle()
                
                red = color.get_active_color().red
                green = color.get_active_color().green
                blue = color.get_active_color().blue
                white = color.get_active_color().white
                
                if red > green and red > blue and red > white: # kontroliert ob es rot ist
                    break
            motor_left.run(-70, True)
            motor_right.run(-70,True)
            

