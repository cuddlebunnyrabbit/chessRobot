import motorlib
import time

motorlib.MotorSys.disable()

#motorlib.MotorSys.just_move(200, 200)


#pawn d4
'''
time.sleep(7)
motorlib.MotorSys.move_to_square("d2")
motorlib.MotorSys.EMSet(True)
motorlib.MotorSys.move_to_square("d4")
motorlib.MotorSys.EMSet(False)
'''

#knight f6
time.sleep(2)
motorlib.MotorSys.move_to_square("g8")
motorlib.MotorSys.EMSet(True)
motorlib.MotorSys.just_move_diag(-142, -142)
motorlib.MotorSys.just_move(0, -285)
motorlib.MotorSys.just_move_diag(-142, -142)
motorlib.MotorSys.EMSet(False)

'''
#bishop h6
time.sleep(5)
motorlib.MotorSys.move_to_square("c1")
motorlib.MotorSys.EMSet(True)
motorlib.MotorSys.just_move_diag(1390, 1390)

time.sleep(2)
motorlib.MotorSys.move_to_square("h4")
motorlib.MotorSys.move_to_square("a4")
motorlib.MotorSys.just_move(-285, 0)
motorlib.MotorSys.EMSet(False)
motorlib.MotorSys.move_to_square("g7")
motorlib.MotorSys.EMSet(True)
motorlib.MotorSys.move_to_square("h6")
motorlib.MotorSys.EMSet(False)
'''


#motorlib.MotorSys.push_move("b1", "c3", True)

motorlib.MotorSys.disable()