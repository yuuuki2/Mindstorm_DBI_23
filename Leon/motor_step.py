import nxt.locator
import nxt.motor
import nxt.locator
import nxt.sensor.generic

# Establish a connection with the NXT brick
with nxt.locator.find() as b: 
    # Initialize the motor
    motor = b.get_motor(nxt.motor.Port.B)

    # Set the power level for the motor
    power = 75

    # Turn 180 degrees to the left
    motor.step(power=power, steps=180, brake=True, regulation_mode=True)
    motor.idle()

    # Turn 180 degrees to the right
    motor.step(power=-power, steps=180, brake=True, regulation_mode=True)
    motor.idle()
