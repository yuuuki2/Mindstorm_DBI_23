import nxt.locator
import nxt.motor
import threading
from threading import Thread

# Funktion zum Bewegen des Motors A
def move_motor_left():
    motor_left.run(power=70)

# Funktion zum Bewegen des Motors B
def move_motor_right():
    motor_right.run(power=70)

# Funktion für die Vorwärtsbewegung
def forward(thread_left, thread_right):
    running = True
    time = 0

    while running:
        # Starte die Threads, um die Motoren gleichzeitig zu bewegen
        thread_left.start()
        thread_right.start()
        time += 1
        if time == 20:
            running = False
            stop_motor.set()

# Funktion für die Linksdrehung
def left(thread_left):
    running = True
    time = 0

    while running:
        thread_left.start()
        time += 1
        if time == 20:
            running = False
            stop_motor.set()

# Funktion für die Rechtsdrehung
def right(thread_right):
    running = True
    time = 0

    while running:
        thread_right.start()
        time += 1
        if time == 20:
            running = False
            stop_motor.set()

# Schaut, ob der Thread angehalten werden soll
stop_motor = threading.Event()

while True:
    with nxt.locator.find() as b:
        motor_left = b.get_motor(nxt.motor.Port.B) # Motor suchen (Port B) und der Variable zuweisen
        motor_right = b.get_motor(nxt.motor.Port.C)# Motor suchen (Port C) und der Variable zuweisen
        
        # Erstelle Threads für die beiden Motoren
        thread_left = Thread(target=move_motor_left)
        thread_right = Thread(target=move_motor_right)

        # Führe die gewünschten Bewegungen aus
        forward_thread = Thread(target=forward, args=(thread_left, thread_right))
        left_thread = Thread(target=left, args=(thread_left,))
        right_thread = Thread(target=right, args=(thread_right,))

        forward_thread.start()
        forward_thread.join()

        left_thread.start()
        left_thread.join()

        right_thread.start()
        right_thread.join()
