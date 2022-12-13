import time
from machine import Pin, PWM, ADC, I2C
import dht

print("\n\n -------------------------- Inicio del programa --------------------------\n\n")

sensor = dht.DHT11(Pin(5))

sensor.measure()
temp = sensor.temperature() 
hum = sensor.humidity()   
text = "Temp: {} Hum: {}".format(temp, hum)

print(text)

def Principal():
    while True:
        time.sleep_ms(1100)
        sensor.measure()
        temp = sensor.temperature() 
        hum = sensor.humidity()   
        text = "Temp: {} Hum: {}".format(temp, hum)
        print(text)

print("\n\n -------------------------- Termino el programa --------------------------\n\n")