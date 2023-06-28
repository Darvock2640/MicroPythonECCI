import time
from machine import ADC, Pin

pot35 = ADC(Pin(35), atten = ADC.ATTN_11DB)
pot35.width(ADC.WIDTH_12BIT)

def main():
    while True:
        value = pot35.read_uv()/1000000
        print(value)
        time.sleep_ms(500)