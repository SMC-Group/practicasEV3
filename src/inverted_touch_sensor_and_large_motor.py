#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.motor import LargeMotor, OUTPUT_B
from ev3dev2.sound import Sound

large_motor = LargeMotor(OUTPUT_B)
ts = TouchSensor()
sd = Sound()
sd.beep()
large_motor.reset()

while True:
    if ts.is_pressed and not large_motor.is_running:
        large_motor.on(50)
    if not ts.is_pressed and large_motor.is_running:
        large_motor.off()