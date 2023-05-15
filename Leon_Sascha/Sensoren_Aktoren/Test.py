import nxt.locator
import nxt.motor
from time import sleep
sock = nxt.locator.find_one_brick()
brick = sock.connect()
motor_a = nxt.motor.Motor(brick, nxt.motor.PORT_B)
print "Initial Position:", motor_a.get_output_state()[7]
motor_a.update( 127, 360, True ) # Turn 360 degrees at full power and brake
motor_a.update( -127, 360 ) # Turn -360 degrees at full power and coast
sleep( 3 ) # update is non-blocking when braking is false, must wait for finish
print( "Final Position:", motor_a.get_output_state()[7])
sock.close()