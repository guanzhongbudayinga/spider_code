# -*- coding: utf-8 -*-

import json
from movement import Movement, MovementMode
from leg import RealLeg
from config import *
from base import point3d
from time import sleep
from servo import Servo
from datetime import datetime


class BaseHexapod(object):
    def __init__(self):
        self._movement = Movement(MovementMode.MOVEMENT_STANDBY.value, False)
        self._mode = MovementMode.MOVEMENT_STANDBY.value


class RealHexapod(BaseHexapod):
    def __init__(self):
        super().__init__()
        self.__leg_servo = Servo(pulse_min=pulse_min, pulse_max=pulse_max)
        self.__legs = [RealLeg(i, self.__leg_servo) for i in range(6)]

    def init(self, setting=False):
        if not setting:
            self.process_movement(MovementMode.MOVEMENT_STANDBY.value)
        print("PiHexa init done.")

    def process_movement(self, mode, elapsed=0):  # 重要函数，与步态执行有关
        if self._mode != mode:
            self._mode = mode
            self._movement.set_mode(self._mode)

        location = self._movement.next(elapsed=elapsed)
        for i in range(6):
            print(location.get(i))
            sleep(1)
            self.__legs[i].move_tip(location.get(i))



