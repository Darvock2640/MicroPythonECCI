import time
from machine import Pin, PWM, ADC, I2C
import sh1106
#import ssd1306
import dht

print("\n\n -------------------------- Inicio del programa --------------------------\n\n")

i2c = I2C(0, scl=Pin(18), sda=Pin(19), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
#display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hola Mundo', 0, 0, 1)
display.show()

def Principal():
    while True:
        pass

print("\n\n -------------------------- Termino el programa --------------------------\n\n")