#!/usr/bin/env python3
from ev3dev2.sensor.lego import GyroSensor

gs = GyroSensor()

while True:
    print(gs.angle)