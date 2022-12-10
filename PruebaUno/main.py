import time
from machine import Pin, PWM, ADC

"""pwm32 = PWM(Pin(32))
pwm32.freq(1500)
pwm32.duty(512)
print(pwm32)"""

adc34 = ADC(Pin(34))

def Principal():
    while True:
        print("El valor en micro voltios es {}".format(adc34.read_uv()))
        print("El valor numérico es {}".format(adc34.read()))
        time.sleep_ms(250)
    

print("\n\n -------------------------- Inicio del programa --------------------------\n\n")



print("\n\n -------------------------- Termino el programa --------------------------\n\n")
