import wpilib
from wpilib.drive import MecanumDrive
from state import state
import oi
import time

import wpilib
from wpilib.drive import MecanumDrive
import time

class MyRobot(wpilib.TimedRobot):

	def robotInit(self):

		self.front_left_motor = wpilib.Talon(0)
		self.rear_left_motor = wpilib.Talon(1)
		self.front_right_motor = wpilib.Talon(2)
		self.rear_right_motor = wpilib.Talon(3)

		self.drive = MecanumDrive(
			self.front_left_motor,
			self.rear_left_motor,
			self.front_right_motor,
			self.rear_right_motor)


	def autonomousPeriodic(self):

		pass

	 
	def teleopPeriodic(self):

		oi.ReadControllerInputs()

		x = state["x_axis"]
		y = state["y_axis"]
		z = state["z_axis"]

		powerX = 0 if x < 0.10 and x > -0.10 else x
		powerY = 0 if y < 0.10 and y > -0.10 else y
		powerZ = 0 if z < 0.10 and z > -0.10 else z

		self.drive.driveCartesian(powerX * 0.6,-powerY * 0.6, powerZ * 0.5, 0)
		

if __name__ == '__main__':
	wpilib.run(MyRobot)
