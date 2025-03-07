#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.motor import LargeMotor, OUTPUT_B

large_motor = LargeMotor(OUTPUT_B)
ts = TouchSensor()

while True:
    if not ts.is_pressed:
        large_motor.on(50)
    else:
        large_motor.off()