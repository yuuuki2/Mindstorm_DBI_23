import nxt.locator
import nxt.motor



with nxt.locator.find() as b: #sucht die Motren und sensoren wenn vorhanden
    motor = b.get_motor(nxt.motor.Port.A)
    
    while True:
        motor.turn(50,45)
        motor.turn(-50,45)
        motor.turn(-50,45)
        motor.turn(50,45)