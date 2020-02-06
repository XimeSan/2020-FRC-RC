import wpilib
from wpilib.drive import MecanumDrive
import time
import oi
from state import state
from networktables import NetworkTables
import threading
import logging


#from ICanSee import VideoRecorder
#import cv2
#import numpy as np
#Rasbperry Ip Adress: 10.57.16.87


class MyRobot(wpilib.TimedRobot):

	def robotInit(self):
		logging.basicConfig(level=logging.DEBUG)
		NetworkTables.initialize()
		self.pc = NetworkTables.getTable("SmartDashboard")
		# self.cond = threading.Condition()
		# self.notified = [False]
		#NetworkTables.initialize(server='roborio-5716-frc.local')
		
		#NetworkTables.initialize()
		#self.sd = NetworkTables.getTable('SmartDashboard')
		# wpilib.CameraServer.launch()
		# cap = cv2.VideoCapture(0)

		# self.Video = VideoRecorder()
		# wpilib.CameraServer.launch()

		self.chasis_controller = wpilib.Joystick(0)

		self.left_cannon_motor = wpilib.Talon(8)
		self.right_cannon_motor = wpilib.Talon(9)

		self.sucker = wpilib.Talon(7)

		self.front_left_motor = wpilib.Talon(3)
		self.rear_left_motor = wpilib.Talon(1)
		self.front_right_motor = wpilib.Talon(4)
		self.rear_right_motor = wpilib.Talon(2)

		self.front_left_motor.setInverted(True)
		self.rear_right_motor.setInverted(True)
		self.rear_left_motor.setInverted(True)


		self.drive = MecanumDrive(
			self.front_left_motor,
			self.rear_left_motor,
			self.front_right_motor,
			self.rear_right_motor)


		#cannon pneumatic
		self.Compressor = wpilib.Compressor(0)
		self.PSV = self.Compressor.getPressureSwitchValue()
		self.cannon_piston = wpilib.Solenoid(0,0)

	def autonomousPeriodic(self):

		position = self.pc.getString("Posicion", "Not jalando")

		print(x)

		wpilib.DriverStation.reportWarning(x,True)

	def teleopPeriodic(self):

		# self.pc = NetworkTables.getTable("Posicion")

		oi.ReadControllerInputs()

		x = state["x_axis"]
		y = state["y_axis"]
		z = state["z_axis"]

		powerX = 0 if x < 0.20 and x > -0.20 else x
		powerY = 0 if y < 0.20 and y > -0.20 else y
		powerZ = 0 if z < 0.20 and z > -0.20 else z

		self.drive.driveCartesian(powerX * -0.7,powerY * 0.7, powerZ * -0.5, 0)

		if state["cannon"]:
			self.right_cannon_motor.set(-1)
			self.left_cannon_motor.set(1)
		else:
			self.right_cannon_motor.set(0)
			self.left_cannon_motor.set(0)

		if state["sucker"]:
			self.sucker.set(0.6)
		else:
			self.sucker.set(0)

		self.cannon_piston.set(state["piston_cannon"])


		# if state["cannon"] != 0:
		# 	self.right_cannon_motor.set(-1)
		# 	self.left_cannon_motor.set(1)
		# else:
		# 	self.right_cannon_motor.set(0)
		# 	self.left_cannon_motor.set(0)

		# if state["sucker"] != 0:
		# 	self.sucker.set(1)
		# else:
		# 	self.sucker.set(0)



	
		if self.PSV:
			self.Compressor.stop()
		else:
			self.Compressor.start()


if __name__ == '__main__':
	wpilib.run(MyRobot)
