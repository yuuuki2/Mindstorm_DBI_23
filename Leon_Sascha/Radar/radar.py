import nxt.locator
import nxt.motor
import nxt.sensor
import nxt.sensor.generic
import matplotlib.pyplot as plt
import numpy as np

with nxt.locator.find() as b:
    motor = b.get_motor(nxt.motor.Port.B)
    sensor = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.generic.Touch)
    us = b.get_sensor(nxt.sensor.Port.S4)

    werte=[]
    werte_back = []
    #Baut den Diagramm zusammen
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar', xlim=(-np.pi/2, np.pi/2))
    ax.set_thetamin(-90)
    ax.set_thetamax(90)
    ax.set_theta_offset(np.pi/2)
    ax.set_thetagrids(np.arange(-90, 91, 15))

    angles = np.linspace(-np.pi/2, np.pi/2, 5)
    
    value = sensor.get_sample()
    while value:
        for i in range(36):
            motor.turn(15, 5) 
            werte.append(us.get_sample())

        values = np.array(werte)
        values_norm = values / 255.0

        if len(werte) == 25:
            ax.plot(angles, values_norm, "o ")
            plt.show()

            for j in range(36):
                motor.turn(-25, 5) 
                werte_back.append(us.get_sample())

            values_back = np.array(werte_back)
            values_back_norm = values_back / 255.0

            if len(werte_back) == 35:
                ax.plot(angles, values_back_norm, "o ")
                plt.show()

            werte.clear()
            werte_back.clear()