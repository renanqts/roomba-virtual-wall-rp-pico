from time import sleep_ms
from machine import Pin, PWM

# Use GPI pin 15
pwm = PWM(Pin(15))

# Set the PWM frequency.
pwm.freq(38000)

# 50% duty
duty = 32512

# The Virtual Walls generate a 1ms ON, 1ms OFF signal continuously
while True:
    pwm.duty_u16(duty)
    sleep_ms(1)
    pwm.duty_u16(-1)
    sleep_ms(1)
