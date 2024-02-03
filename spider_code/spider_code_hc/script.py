import numpy as np
from time import sleep
import time
from adafruit_servokit import ServoKit

class Spider:
    def __init__(self):
        """Initialize spider
        """
        self.deg1,self.deg2,self.deg3 = 90, 70, 90
        self.hat1 = ServoKit(channels=16, address = 0x40)
        self.hat2 = ServoKit(channels=16, address = 0x41)
        self.leg_1 = [self.hat1, [0,1,2], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_2 = [self.hat1, [3,4,5], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_3 = [self.hat1, [6,7,8], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_4 = [self.hat2, [0,1,2], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_5 = [self.hat2, [3,4,5], np.array([self.deg1,self.deg2,self.deg3])]
        self.leg_6 = [self.hat2, [6,7,8], np.array([self.deg1,self.deg2,self.deg3])]
        self.legs = [self.leg_1, self.leg_2, self.leg_3, self.leg_4, self.leg_5, self.leg_6]
        self.start_position()

    def move_single_leg(self, arr_deg, index_leg):
        """_summary_

        Args:
            arr_deg (arr): array with wanted angles for  all 3 servos 
            leg (index): arr with information about leg hat, pins, angles.
        """        
        hat, channels, _ = self.legs[index_leg]
        hat.servo[channels[0]].angle = arr_deg[0]
        hat.servo[channels[1]].angle = arr_deg[1]
        hat.servo[channels[2]].angle = arr_deg[2]
        self.legs[index_leg][2] = arr_deg
    
    def move_all_legs(self,arr_deg):
        """just simple calling move single leg function for all legs

        Args:
            arr_deg (arr): wanted angles for all legs
        """        
        for i, leg in enumerate(self.legs):
            self.move_single_leg(arr_deg=arr_deg, index_leg=i)

    def start_position(self):
        """Position where the spider is standing stable
        """        
        self.move_all_legs([self.deg1,self.deg2,self.deg3])

    def change_single(self, index_leg, change_deg):
        """Function that will change the angles of a single leg

        Args:
            leg (arr): Array with information about the leg
            change_deg (arr): angles that the leg needs to be changed too
        """        
        _, _, current_deg = self.legs[index_leg]
        # up 
        self.move_single_leg([current_deg[0], current_deg[1] + 30, current_deg[2]], index_leg)
        sleep(.1)
        self.move_single_leg([current_deg[0] + change_deg, current_deg[1] + 30, current_deg[2]], index_leg)
        sleep(.1)
        self.move_single_leg([current_deg[0] + change_deg, current_deg[1], current_deg[2]], index_leg)
    
    def reset_pos(self):
        """function that will reset all horizontal moving servos to 90 degrees
        """        
        self.move_single_leg([90,self.leg_1[2][1], self.leg_1[2][2]], 0)
        self.move_single_leg([90,self.leg_2[2][1], self.leg_2[2][2]], 1)
        self.move_single_leg([90,self.leg_3[2][1], self.leg_3[2][2]], 2)
        self.move_single_leg([90,self.leg_4[2][1], self.leg_4[2][2]], 3)
        self.move_single_leg([90,self.leg_5[2][1], self.leg_5[2][2]], 4)
        self.move_single_leg([90,self.leg_6[2][1], self.leg_6[2][2]], 5)


    def change_all(self, change_deg):
        """just simple calling change single leg function for all legs

        Args:
            change_deg (_type_): _description_
        """        
        for i,leg in enumerate(self.legs):
            self.change_single(index_leg=i, change_deg=change_deg)
            sleep(.1)


    def tripod_walk_2(self, steps=1):
        """Moves three legs at the same time in tripod formation.

        Args:
            steps (int, optional): Amount of steps. Defaults to 1.
        """        
        start_values_1 = self.leg_1[2]
        start_values_2 = self.leg_2[2]
        start_values_3 = self.leg_3[2]
        start_values_4 = self.leg_4[2]
        start_values_5 = self.leg_5[2]
        start_values_6 = self.leg_6[2]
        
        for _ in range(steps):
            # Reset legs 1, 3 & 5, whilst moving 0, 2 & 4
            sleep(.1)
            self.move_single_leg(start_values_2,1)
            self.move_single_leg(start_values_4,3)
            self.move_single_leg(start_values_6,5)
            self.move_single_leg([start_values_1[0], start_values_1[1]+30, start_values_1[2]], 0)
            self.move_single_leg([start_values_3[0], start_values_3[1]+30, start_values_3[2]], 2)
            self.move_single_leg([start_values_5[0], start_values_5[1]+30, start_values_5[2]], 4)
            sleep(.1)
            self.move_single_leg([start_values_1[0]+45, start_values_1[1]+30, start_values_1[2]], 0)
            self.move_single_leg([start_values_3[0]+45, start_values_3[1]+30, start_values_3[2]], 2)
            self.move_single_leg([start_values_5[0]-45, start_values_5[1]+30, start_values_5[2]], 4)
            sleep(.1)
            self.move_single_leg([start_values_1[0]+45, start_values_1[1], start_values_1[2]], 0)
            self.move_single_leg([start_values_3[0]+45, start_values_3[1], start_values_3[2]], 2)
            self.move_single_leg([start_values_5[0]-45, start_values_5[1], start_values_5[2]], 4)
            sleep(1)
            
            # Reset legs 0, 2 & 4, whilst moving 1, 3 & 5
            self.move_single_leg(start_values_1,0)
            self.move_single_leg(start_values_3,2)
            self.move_single_leg(start_values_5,4)
            self.move_single_leg([start_values_2[0], start_values_2[1]+30, start_values_2[2]], 1)
            self.move_single_leg([start_values_4[0], start_values_4[1]+30, start_values_4[2]], 3)
            self.move_single_leg([start_values_6[0], start_values_6[1]+30, start_values_6[2]], 5)
            sleep(.1)
            self.move_single_leg([start_values_2[0]+45, start_values_2[1]+30, start_values_2[2]], 1)
            self.move_single_leg([start_values_4[0]-45, start_values_4[1]+30, start_values_4[2]], 3)
            self.move_single_leg([start_values_6[0]-45, start_values_6[1]+30, start_values_6[2]], 5)
            sleep(.1)
            self.move_single_leg([start_values_2[0]+45, start_values_2[1], start_values_2[2]], 1)
            self.move_single_leg([start_values_4[0]-45, start_values_4[1], start_values_4[2]], 3)
            self.move_single_leg([start_values_6[0]-45, start_values_6[1], start_values_6[2]], 5)
            sleep(1)
            
        # Reset legs to starting position
        self.move_single_leg(start_values_1,0)
        self.move_single_leg(start_values_2,1)
        self.move_single_leg(start_values_3,2)
        self.move_single_leg(start_values_4,3)
        self.move_single_leg(start_values_5,4)
        self.move_single_leg(start_values_6,5)
            
        
    def walk1(self, steps):
        start_values_1 = self.leg_1[2]
        start_values_2 = self.leg_2[2]
        start_values_3 = self.leg_3[2]
        start_values_4 = self.leg_4[2]
        start_values_5 = self.leg_5[2]
        start_values_6 = self.leg_6[2]
        for _ in range(steps):
            # Lift and move legs 0, 2, & 4
            sleep(.1)
            self.change_single(0, 45)
            self.change_single(2, 45)
            self.change_single(4, -45)
            sleep(.2)
            
            # Reset legs to start position
            self.move_single_leg([start_values_2[0], start_values_2[1]+30, start_values_2[2]], 1)
            #self.move_single_leg([start_values_4[0], start_values_4[1]+30, start_values_4[2]], 3)
            self.move_single_leg([start_values_6[0], start_values_6[1]+30, start_values_6[2]], 5)
            sleep(.2)
            self.move_single_leg(start_values_1,0)
            self.move_single_leg(start_values_3,2)
            self.move_single_leg(start_values_4,3)
            self.move_single_leg(start_values_5,4)
            sleep(.2)
            self.move_single_leg(start_values_2,1)
            self.move_single_leg(start_values_6,5)
            
            # Lift and move legs 1, 3, & 5
            self.change_single(1, 45)
            self.change_single(3, -45)
            self.change_single(5, -45)
            sleep(.2)
            
            # Reset legs to start position
            self.move_single_leg([start_values_1[0], start_values_1[1]+30, start_values_1[2]], 0)
            #self.move_single_leg([start_values_3[0], start_values_3[1]+30, start_values_3[2]], 2)
            self.move_single_leg([start_values_5[0], start_values_5[1]+30, start_values_5[2]], 4)
            sleep(.2)
            self.move_single_leg(start_values_2,1)
            self.move_single_leg(start_values_3,2)
            self.move_single_leg(start_values_4,3)
            self.move_single_leg(start_values_6,5)
            sleep(.2)
            self.move_single_leg(start_values_1,0)
            self.move_single_leg(start_values_5,4)


    def turn3_0(self,steps, direction, speed = .5):
        
        if direction == 'right':
            angle = -30
            go = True
        elif direction == 'left':
            angle = 30
            go = True
        else:
            print('what direction is the turn, right or left?')
            go = False
            
        if go:
            start_values_1 = self.leg_1[2]
            start_values_2 = self.leg_2[2]
            start_values_3 = self.leg_3[2]
            start_values_4 = self.leg_4[2]
            start_values_5 = self.leg_5[2]
            start_values_6 = self.leg_6[2]
            for _ in range(steps):
                # Lift and move legs 0,1, 2 3, 4, 5 forward
                for leg_index in [0, 3, 4,2,1, 5]:
                    self.change_single(leg_index, angle)
                    time.sleep(speed)

                # Reset legs to starting position
                self.move_single_leg(start_values_1,0)
                self.move_single_leg(start_values_2,1)
                self.move_single_leg(start_values_3,2)
                self.move_single_leg(start_values_4,3)
                self.move_single_leg(start_values_5,4)
                self.move_single_leg(start_values_6,5)


    def walk_forward(self, steps, speed=0.5):
        start_values_1 = self.leg_1[2]
        start_values_2 = self.leg_2[2]
        start_values_3 = self.leg_3[2]
        start_values_4 = self.leg_4[2]
        start_values_5 = self.leg_5[2]
        start_values_6 = self.leg_6[2]
        for _ in range(steps):
            # Lift and move legs 0, 3, 4 forward
            for i in range(30):
                self.change_single(0,i)
                

                self.change_single(4,-i)
                

                self.change_single(3,-i)
                time.sleep(speed)

            # Reset legs to starting position
            self.move_single_leg(start_values_1,0)
            self.move_single_leg(start_values_2,1)
            self.move_single_leg(start_values_3,2)
            self.move_single_leg(start_values_4,3)
            self.move_single_leg(start_values_5,4)
            self.move_single_leg(start_values_6,5)

            for i in range(30):
                self.change_single(5,-i)
               

                # Lift and move legs 1, 2, 5 forward
                self.change_single(1,i)
               

                self.change_single(2,i)
                time.sleep(speed)

            # Reset legs to starting position
            self.move_single_leg(start_values_1,0)
            self.move_single_leg(start_values_2,1)
            self.move_single_leg(start_values_3,2)
            self.move_single_leg(start_values_4,3)
            self.move_single_leg(start_values_5,4)
            self.move_single_leg(start_values_6,5)

    def walk_forward_diagonal(self, steps, speed=0.5):
        start_values_1 = self.leg_1[2]
        start_values_2 = self.leg_2[2]
        start_values_3 = self.leg_3[2]
        start_values_4 = self.leg_4[2]
        start_values_5 = self.leg_5[2]
        start_values_6 = self.leg_6[2]
        for _ in range(steps):
            # Lift and move legs 0, 1 & 4 forward
            self.change_single(0, 30)
            self.change_single(4, -30)
            self.change_single(1, 30)
            time.sleep(speed)

            # Reset legs to starting position
            self.move_single_leg(start_values_1,0)
            self.move_single_leg(start_values_2,1)
            self.move_single_leg(start_values_3,2)
            self.move_single_leg(start_values_4,3)
            self.move_single_leg(start_values_5,4)
            self.move_single_leg(start_values_6,5)
            sleep(.1)

            # Lift and move legs 2, 3 & 5 forward
            self.change_single(3, -30)
            self.change_single(2, 30)
            self.change_single(5, -30)
            time.sleep(speed)

            # Reset legs to starting position
            self.move_single_leg(start_values_1,0)
            self.move_single_leg(start_values_2,1)
            self.move_single_leg(start_values_3,2)
            self.move_single_leg(start_values_4,3)
            self.move_single_leg(start_values_5,4)
            self.move_single_leg(start_values_6,5)
            sleep(.1)

    def walk_four(self, steps=1, speed=0.5):
        start_values_1 = self.leg_1[2]
        start_values_2 = self.leg_2[2]
        start_values_3 = self.leg_3[2]
        start_values_4 = self.leg_4[2]
        start_values_5 = self.leg_5[2]
        start_values_6 = self.leg_6[2]
        
        for _ in range(steps):
            self.change_single(0, 45)
            self.change_single(5, -45)
            sleep(speed)
            self.change_single(2, 45)
            self.change_single(3, -45)
            sleep(speed)
            self.move_single_leg([start_values_2[0], start_values_2[1]+30, start_values_2[2]], 1)
            self.move_single_leg([start_values_5[0], start_values_5[1]+30, start_values_5[2]], 4)
            self.move_single_leg(start_values_1, 0)
            self.move_single_leg(start_values_3, 2)
            self.move_single_leg(start_values_4, 3)
            self.move_single_leg(start_values_6, 5)
            sleep(speed)
            self.move_single_leg(start_values_2, 1)
            self.move_single_leg(start_values_5, 4)


    def tripod_turn(self, steps, direction, speed = 0.5, height = 30):
        if direction == 'right':
            angle = -30
            go = True
        elif direction == 'left':
            angle = 30
            go = True

        else:
            print('what direction is the turn, right or left?')
            go = False
        if go:
            start_values_1 = self.leg_1[2]
            start_values_2 = self.leg_2[2]
            start_values_3 = self.leg_3[2]
            start_values_4 = self.leg_4[2]
            start_values_5 = self.leg_5[2]
            start_values_6 = self.leg_6[2]
            for _ in range(steps):
                # Lift and move all legs forward
                for leg_index in [[0, 2, 4], [1, 3, 5]]:
                    _, _, current_deg_1 = self.legs[leg_index[0]]
                    _, _, current_deg_2 = self.legs[leg_index[1]]
                    _, _, current_deg_3 = self.legs[leg_index[2]]

                    self.move_single_leg([current_deg_1[0], current_deg_1[1] + height, current_deg_1[2]], leg_index[0])
                    self.move_single_leg([current_deg_2[0], current_deg_2[1] + height, current_deg_2[2]], leg_index[1])
                    self.move_single_leg([current_deg_3[0], current_deg_3[1] + height, current_deg_3[2]], leg_index[2])
                    
                    self.reset_pos()
                    
                    sleep(speed)
                    self.move_single_leg([current_deg_1[0] + angle, current_deg_1[1] + height, current_deg_1[2]], leg_index[0])
                    self.move_single_leg([current_deg_2[0] + angle, current_deg_2[1] + height, current_deg_2[2]], leg_index[1])
                    self.move_single_leg([current_deg_3[0] + angle, current_deg_3[1] + height, current_deg_3[2]], leg_index[2])
                    
                    sleep(speed)
                    self.move_single_leg([current_deg_1[0] + angle, current_deg_1[1], current_deg_1[2]], leg_index[0])
                    self.move_single_leg([current_deg_2[0] + angle, current_deg_2[1], current_deg_2[2]], leg_index[1])
                    self.move_single_leg([current_deg_3[0] + angle, current_deg_3[1], current_deg_3[2]], leg_index[2])
                    
                    time.sleep(speed)

            self.move_single_leg([self.legs[0][2][0], self.legs[0][2][1] + height, self.legs[0][2][2]], 0)
            self.move_single_leg([self.legs[2][2][0], self.legs[2][2][1] + height, self.legs[2][2][2]], 2)
            self.move_single_leg([self.legs[4][2][0], self.legs[4][2][1] + height, self.legs[4][2][2]], 4)
            sleep(.1)
            self.reset_pos()
            sleep(.1)
            self.move_single_leg(start_values_1,0)
            self.move_single_leg(start_values_3,2)
            self.move_single_leg(start_values_5,4)


    def calc_changing_deg(self, leg_index, wanted_degrees, N):
        changing_deg2_1 = wanted_degrees[0] - self.legs[leg_index][2][1]
        changing_deg3_1 = wanted_degrees[1] - self.legs[leg_index][2][2]

        step_deg1 = changing_deg2_1/N
        step_deg2 = changing_deg3_1/N

        return step_deg1, step_deg2


    def sit_stand_steps_2(self, N=100, delay=.01, wanted_degrees = [175,162]):
        # Sitdown = [90, 10]
        # Standup = [0, 60]
        run = False
        try:
            run = True
            deg_stand_steps_2_1, deg_stand_steps_3_1 = self.calc_changing_deg(0, wanted_degrees, N)
            deg_stand_steps_2_2, deg_stand_steps_3_2 = self.calc_changing_deg(1, wanted_degrees, N)
            deg_stand_steps_2_3, deg_stand_steps_3_3 = self.calc_changing_deg(2, wanted_degrees, N)
            deg_stand_steps_2_4, deg_stand_steps_3_4 = self.calc_changing_deg(3, wanted_degrees, N)
            deg_stand_steps_2_5, deg_stand_steps_3_5 = self.calc_changing_deg(4, wanted_degrees, N)
            deg_stand_steps_2_6, deg_stand_steps_3_6 = self.calc_changing_deg(5, wanted_degrees, N)
        except:
            print('something went wrong')

        if run:
            for _ in range(N):
                self.move_single_leg([self.leg_1[2][0],self.leg_1[2][1]+deg_stand_steps_2_1,self.leg_1[2][2]+deg_stand_steps_3_1], 0)
                self.move_single_leg([self.leg_2[2][0],self.leg_2[2][1]+deg_stand_steps_2_2,self.leg_2[2][2]+deg_stand_steps_3_2], 1)
                self.move_single_leg([self.leg_3[2][0],self.leg_3[2][1]+deg_stand_steps_2_3,self.leg_3[2][2]+deg_stand_steps_3_3], 2)
                self.move_single_leg([self.leg_4[2][0],self.leg_4[2][1]+deg_stand_steps_2_4,self.leg_4[2][2]+deg_stand_steps_3_4], 3)
                self.move_single_leg([self.leg_5[2][0],self.leg_5[2][1]+deg_stand_steps_2_5,self.leg_5[2][2]+deg_stand_steps_3_5], 4)
                self.move_single_leg([self.leg_6[2][0],self.leg_6[2][1]+deg_stand_steps_2_6,self.leg_6[2][2]+deg_stand_steps_3_6], 5)
                sleep(delay)
    def move_up(self):
        wanted_degrees= [self.leg_1[2][1]-14,self.leg_1[2][2]-6]
        self.sit_stand_steps_2(100,0.01,wanted_degrees)
        
    def move_down(self):
        wanted_degrees= [self.leg_1[2][1]+4,self.leg_1[2][2]-16]
        self.sit_stand_steps_2(100,0.01,wanted_degrees)
    
    def face_up(self, speed = .5):
        self.move_single_leg([60,0,30],1)
        self.move_single_leg([120,0,30],0)

        self.move_single_leg([90,60,60],2)
        self.move_single_leg([90,60,60],5)

        self.move_single_leg([60,60,60],1)
        self.move_single_leg([120,60,60],4)

    def bottom_up(self, speed = .5):
        self.move_single_leg([60,0,30],2)
        self.move_single_leg([120,0,30],3)

        self.move_single_leg([60,90,60],0)
        self.move_single_leg([120,60,60],5)

        self.move_single_leg([60,60,60],4)
        self.move_single_leg([120,60,60],1)
    
    def sleep_modus(self):
        self.sit_stand_steps_2(100,0,[175,162])
        
    def wave(self, duration):
        start_time = time.time()
        waving = True
        start_values_1 = self.leg_1[2]
        while waving:
            
            self.move_single_leg([spin.leg_1[2][0], 180, 00], 0)
            time.sleep(.5)
            self.move_single_leg([spin.leg_1[2][0], 180, 110], 0)
            time.sleep(.5)
            
            # Current time
            current_time = time.time()

            # Elapsed time
            elapsed_time = current_time - start_time

            # Remaining time
            remaining_time = duration - elapsed_time

            # Check if the timer has reached its duration
            if remaining_time <= 0:
                print("Timer completed.")
                waving = False
                self.move_single_leg(start_values_1, 0)

    def walk_sideways(self, steps=1, delay=1):
        self.move_single_leg([150, 70, 90], 0)
        self.move_single_leg([30, 70, 90], 1)
        self.move_single_leg([150, 70, 90], 2)
        self.move_single_leg([120, 70, 90], 3)
        self.move_single_leg([90, 70, 90], 4)
        self.move_single_leg([60, 70, 90], 5)

        for _ in range(steps):
            self.move_single_leg([90, 70, 90], 1)
            self.move_single_leg([30, 70, 90], 3)
            self.move_single_leg([150, 70, 90], 5)
            self.move_single_leg([30, 100, 90], 0)
            self.move_single_leg([150, 100, 90], 2)
            self.move_single_leg([90, 100, 90], 4)
            sleep(delay)
            self.move_single_leg([30, 100, 60], 0)
            self.move_single_leg([150, 100, 60], 2)
            self.move_single_leg([90, 100, 120], 4)
            sleep(delay)
            self.move_single_leg([30, 70, 60], 0)
            self.move_single_leg([150, 70, 60], 2)
            self.move_single_leg([90, 70, 120], 4)
            sleep(delay)
            self.move_single_leg([90, 100, 90], 1)
            self.move_single_leg([30, 100, 90], 3)
            self.move_single_leg([150, 100, 90], 5)
            self.move_single_leg([30, 70, 90], 0)
            self.move_single_leg([150, 70, 90], 2)
            self.move_single_leg([90, 70, 90], 4)
            sleep(delay)
            self.move_single_leg([90, 100, 60], 1)
            self.move_single_leg([30, 100, 120], 3)
            self.move_single_leg([150, 100, 120], 5)
            sleep(delay)
            self.move_single_leg([90, 70, 60], 1)
            self.move_single_leg([30, 70, 120], 3)
            self.move_single_leg([150, 70, 120], 5)
            sleep(delay)

        self.move_single_leg([30, 70, 90], 0)
        self.move_single_leg([90, 70, 90], 1)
        self.move_single_leg([150, 70, 90], 2)
        self.move_single_leg([30, 70, 90], 3)
        self.move_single_leg([90, 70, 90], 4)
        self.move_single_leg([150, 70, 90], 5)

    def walk_please(self,degrees = 25, speed = .1, N = 2, height = 30):
        step = 0
        first_time = True
        for i in range(N):
            step += 1
            
            if first_time:
            # First move up and angle
            
                first_time = False
                self.move_single_leg([self.leg_1[2][0], self.leg_1[2][1]+ height,self.leg_1[2][2]],0)
                self.move_single_leg([self.leg_3[2][0], self.leg_3[2][1]+ height,self.leg_3[2][2]],2)
                self.move_single_leg([self.leg_5[2][0], self.leg_5[2][1]+ height,self.leg_5[2][2]],4)
                
                time.sleep(speed)
                
                self.move_single_leg([self.leg_1[2][0] - degrees, self.leg_1[2][1],self.leg_1[2][2]],0)
                self.move_single_leg([self.leg_3[2][0] + degrees, self.leg_3[2][1],self.leg_3[2][2]],2)
                self.move_single_leg([self.leg_5[2][0] - degrees, self.leg_5[2][1],self.leg_5[2][2]],4)
            
                time.sleep(speed)
                
            
            self.move_single_leg([self.leg_1[2][0], self.leg_1[2][1] - height ,self.leg_1[2][2]],0)
            self.move_single_leg([self.leg_3[2][0], self.leg_3[2][1] - height ,self.leg_3[2][2]],2)
            self.move_single_leg([self.leg_5[2][0], self.leg_5[2][1] - height ,self.leg_5[2][2]],4)
            
            time.sleep(speed)
            
            #second move up and angle
            
            self.move_single_leg([self.leg_2[2][0], self.leg_2[2][1] + height ,self.leg_2[2][2]],1)
            self.move_single_leg([self.leg_4[2][0], self.leg_4[2][1] + height ,self.leg_4[2][2]],3)
            self.move_single_leg([self.leg_6[2][0], self.leg_6[2][1] + height ,self.leg_6[2][2]],5)
            
            time.sleep(speed)
    
            self.move_single_leg([self.leg_2[2][0] + degrees, self.leg_2[2][1], self.leg_2[2][2]],1)
            self.move_single_leg([self.leg_4[2][0] + degrees, self.leg_4[2][1], self.leg_4[2][2]],3)
            self.move_single_leg([self.leg_6[2][0] - degrees, self.leg_6[2][1], self.leg_6[2][2]],5)
            
            time.sleep(speed)
            
            self.move_single_leg([90, self.leg_1[2][1], self.leg_1[2][2]],0)
            self.move_single_leg([90, self.leg_3[2][1], self.leg_3[2][2]],2)
            self.move_single_leg([90, self.leg_5[2][1], self.leg_5[2][2]],4)
            
            time.sleep(speed)
            
            if step == N:
                self.move_single_leg([self.leg_2[2][0] - degrees, self.leg_2[2][1] - 30,self.leg_2[2][2]],1)
                self.move_single_leg([self.leg_4[2][0] - degrees, self.leg_4[2][1] - 30,self.leg_4[2][2]],3)
                self.move_single_leg([self.leg_6[2][0] + degrees, self.leg_6[2][1] - 30,self.leg_6[2][2]],5)
            else:
                self.move_single_leg([self.leg_2[2][0], self.leg_2[2][1] - height,self.leg_2[2][2]],1)
                self.move_single_leg([self.leg_4[2][0], self.leg_4[2][1] - height,self.leg_4[2][2]],3)
                self.move_single_leg([self.leg_6[2][0], self.leg_6[2][1] - height,self.leg_6[2][2]],5)
                
                time.sleep(speed)
                
                self.move_single_leg([self.leg_1[2][0], self.leg_1[2][1]+ height,self.leg_1[2][2]],0)
                self.move_single_leg([self.leg_3[2][0], self.leg_3[2][1]+ height,self.leg_3[2][2]],2)
                self.move_single_leg([self.leg_5[2][0], self.leg_5[2][1]+ height,self.leg_5[2][2]],4)
                
                time.sleep(speed)
                
                self.move_single_leg([self.leg_1[2][0] - degrees, self.leg_1[2][1],self.leg_1[2][2]],0)
                self.move_single_leg([self.leg_3[2][0] + degrees, self.leg_3[2][1],self.leg_3[2][2]],2)
                self.move_single_leg([self.leg_5[2][0] - degrees, self.leg_5[2][1],self.leg_5[2][2]],4)
                
                time.sleep(speed)
                
                self.move_single_leg([90, self.leg_2[2][1],self.leg_2[2][2]], 1)
                self.move_single_leg([90, self.leg_4[2][1],self.leg_4[2][2]], 3)
                self.move_single_leg([90, self.leg_6[2][1],self.leg_6[2][2]], 5)
                

                
                
    def walk_sideway(self, steps=1, delay=1):
        self.move_single_leg([150, 70, 90], 0)
        self.move_single_leg([30, 70, 90], 1)
       
        self.move_single_leg([120, 70, 90], 3)
        self.move_single_leg([60, 70, 90], 4)
          
            
            
                
                
                
                
                
                
                
            
            
            
            

                
            
    def walk_please_2(self,degrees = 15, speed = .5):
            
            self.move_single_leg([self.leg_1[2][0], self.leg_1[2][1]+ 30,self.leg_1[2][2]],0)
            self.move_single_leg([self.leg_3[2][0], self.leg_3[2][1]+ 30,self.leg_3[2][2]],2)
            self.move_single_leg([self.leg_5[2][0], self.leg_5[2][1]+ 30,self.leg_5[2][2]],4)
            
            time.sleep(speed)
            
            self.move_single_leg([self.leg_1[2][0] - degrees, self.leg_1[2][1] - 30,self.leg_1[2][2]],0)
            self.move_single_leg([self.leg_3[2][0] + degrees, self.leg_3[2][1] - 30,self.leg_3[2][2]],2)
            self.move_single_leg([self.leg_5[2][0] - degrees, self.leg_5[2][1] - 30,self.leg_5[2][2]],4)
            
            time.sleep(speed)

    
        

spin = Spider()





a=1