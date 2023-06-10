import nxt.sensor
import nxt.sensor.generic
import nxt.sensor.hitechnic
import nxt.locator
import nxt.motor
import time

def color_rgb():
    red = color.get_active_color().red
    green = color.get_active_color().green
    blue = color.get_active_color().blue
    white = color.get_active_color().white
    return  red,green,blue,white

def color_sens(red,green,blue,white, line_color,a):
    color_checks = {
        "red": lambda: red > green and red > blue and red > white,
        "green": lambda: green > red and green > blue and green > white,
        "blue": lambda: blue > red and blue > green and blue > white
    }
    
    
    if color_checks[line_color]():
        control(motor_left, motor_right, 0)
        con = 1
        return con 

    elif a < 40 :

        control(motor_left, motor_right, 1)
        
    elif a > 39 and a < 120:
        
        control(motor_left, motor_right, 2)
    else:
        con = 1
        return con
            
    
            
def control(motor_left,motor_right,controll_number):
    speed = 70
    if controll_number == 0: #forward
        motor_left.run(-speed, True)
        motor_right.run(-speed, True)
        
    elif controll_number == 1: #left
        motor_left.turn(speed, 5)
        motor_right.turn(-speed, 5)
            
    elif controll_number == 2: #right
        motor_left.turn(-speed, 5)
        motor_right.turn(speed, 5) 
            
            
    
  

with nxt.locator.find() as b:
    motor_left = b.get_motor(nxt.motor.Port.A)
    motor_right = b.get_motor(nxt.motor.Port.B)
    touch = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.generic.Touch)
    color = b.get_sensor(nxt.sensor.Port.S3, nxt.sensor.hitechnic.Colorv2)
    
    line_color = "red"
    a = 0
    
    while True:
        value = touch.get_sample()
        if value == True:
            a += 1
            red,green,blue,white = color_rgb()
            cont = color_sens(red,green,blue,white,line_color,a)
            if cont == 1:
                a = 0
