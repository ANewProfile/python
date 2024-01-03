from hub import port
import motor_pair
import color_sensor
import math
import time
import runloop

async def main():
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1, port.D, port.C)
    while True:
        motor_pair.move(motor_pair.PAIR_1, (math.floor(-3/5)*color_sensor.reflection(port.B)+30), velocity=280)
    
    motor_pair.stop(motor_pair.PAIR_1)