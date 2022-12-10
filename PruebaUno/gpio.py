import time
from machine import Pin, PWM

def Principal():

    gpio4 = Pin(4, Pin.OUT)

    while True:
        print("Encender Pin")
        gpio4.on()
        time.sleep_ms(125)
        print("Apagar Pin")
        gpio4.off()
        time.sleep_ms(125)

print("\n\n -------------------------- Inicio del programa --------------------------\n\n")



print("\n\n -------------------------- Termino el programa --------------------------\n\n")
