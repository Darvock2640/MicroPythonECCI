import time
from machine import ADC, Pin

accX = ADC(Pin(12), atten = ADC.ATTN_11DB)
accX.width(ADC.WIDTH_12BIT)

accY = ADC(Pin(13), atten = ADC.ATTN_11DB)
accY.width(ADC.WIDTH_12BIT)

def main():
    while True:
        valueX = accX.read_uv() - 1670000
        valueY = accY.read_uv() - 1660000
        print("X: {}, Y: {}".format(valueX,valueY))
        time.sleep_ms(500)