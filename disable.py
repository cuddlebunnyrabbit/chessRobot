import motorlib
import time

motorlib.MotorSys.disable()
motorlib.MotorSys.EMSet(False)
'''
motorlib.MotorSys.move_to_square("d2")
motorlib.MotorSys.EMSet(True)
time.sleep(5)
motorlib.MotorSys.EMSet(False)
motorlib.MotorSys.move_to_square("h1")
'''
#motorlib.MotorSys.just_move(-200, -200)
#motorlib.MotorSys.push_move("a2", "a4", False)