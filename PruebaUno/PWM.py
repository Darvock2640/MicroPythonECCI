import time
from machine import Pin, PWM, ADC

pwm32 = PWM(Pin(32))
pwm32.freq(1500)
pwm32.duty(512)
print(pwm32)