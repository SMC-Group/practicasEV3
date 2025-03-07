#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B
from ev3dev2.button import Button

large_motor = LargeMotor(OUTPUT_B)
btn = Button()
while not btn.any():
    large_motor.on(50)
large_motor.off()
exit()