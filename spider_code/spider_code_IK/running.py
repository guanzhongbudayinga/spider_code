# -*- coding: utf-8 -*-

import _thread
from time import time, sleep
from hexapod import RealHexapod
from movement import MovementMode

from config import movement_interval


DEBUG = False
REACT_DELAY = movement_interval * 0.001
loop_mode = 1  # default normal-loop


def normal_loop():
    for i in range(10):
        pi_hexa.process_movement(MovementMode.MOVEMENT_FORWARD.value)
        sleep(1)
        pi_hexa.process_movement(MovementMode.MOVEMENT_FORWARD.value)


if __name__ == '__main__':
    # Hexapod instance
    pi_hexa = RealHexapod()
    pi_hexa.init()
    pi_hexa.__legs[0].move_tip(58,89,0)
    normal_loop()
