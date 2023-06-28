from hcsr04 import HCSR04
import time

ultraSonido = HCSR04(trigger_pin=32, echo_pin=33)

def main():
    while True:
        distance = ultraSonido.distance_cm()
        print("La distancia es {}cm".format(distance))
        time.sleep(1)