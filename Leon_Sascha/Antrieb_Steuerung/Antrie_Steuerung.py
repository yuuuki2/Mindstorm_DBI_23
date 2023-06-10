import nxt.locator
import nxt.motor, time

def forward(motor_left,motor_right,speed,num):
    # forward
    motor_left.run(-speed)
    motor_right.run(-speed)
        
    time.sleep(num)
    motor_left.idle()
    motor_right.idle()

def left(motor_left,motor_right,speed,num):
    # links drehen
    motor_left.run(speed)
    motor_right.run(-speed)
        
    time.sleep(num)
    motor_left.idle()
    motor_right.idle()

def right(motor_left,motor_right,speed,num):
    # rechts drehen
    motor_left.run(-speed)
    motor_right.run(speed)
        
    time.sleep(num+num)
    motor_left.idle()
    motor_right.idle()

with nxt.locator.find() as b: #sucht die Motren und sensoren wenn vorhanden
    motor_left = b.get_motor(nxt.motor.Port.A) # Motor suchen (Port B) und der Variable zuweisen
    motor_right = b.get_motor(nxt.motor.Port.B)#
    
    speed = 70
    num = 5
    
    running = True
    while running:

        
        left(motor_left,motor_right,speed,num)
        right(motor_left,motor_right,speed,num)
        

        
        running = False
    
    
