# import time
# import VL53L1X

# tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
# tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)


# tof1.open()
# tof2.open()

# try:
#     while True:
#         dis1 = tof1.get_distance()
#         dis2 = tof2.get_distance()
#         print(f"Distance1: {dis1}mm")
#         print(f"Distance2: {dis2}mm")
#         time.sleep(0.5)
# except:
#     tof1.stop_ranging()
#     tof2.stop_ranging()
#     tof1.close()
#     tof2.close()

import busio,board, time, adafruit_vl53l1x

i2c = board.I2C()
tof1 = adafruit_vl53l1x.VL53L1X(i2c, address=0x29, channels=2)
# i2c2 = busio.I2C(board.SDA_1, board.SCL_1)
# tof2 = adafruit_vl53l1x.VL53L1X(i2c2, address=0x30)

tof1.set_address(0x29)
# tof2.set_address(0x30)

tof1.start_ranging()
tof2.start_ranging()

while True:
    print(f"dis: {tof1.distance}")
    print(f"dis: {tof2.distance}")
    tof1.clear_interrupt()
    tof2.clear_interrupt()
    time.sleep(.5)