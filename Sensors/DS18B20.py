import time, ds18x20
import onewire
from machine import Pin

ow = onewire.OneWire(Pin(12))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
sensor = roms[0]

def main():
    while True:
        ds.convert_temp()
        time.sleep_ms(750)
        print(ds.read_temp(sensor))

