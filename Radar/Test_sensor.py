
#!/usr/bin/env python3
"""NXT-Python example to use sensors."""
import time
import nxt.locator
import nxt.sensor
import nxt.sensor.generic

with nxt.locator.find() as b:
    us = b.get_sensor(nxt.sensor.Port.S4)

    while True:
        samples = us.get_sample()
        print(samples)
        time.sleep(0.5)