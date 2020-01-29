import wpilib
from wpilib.drive import MecanumDrive
from state import state
import oi
import time
from networktables import NetworkTables
#from ICanSee import VideoRecorder
#import cv2

class MyRobot(wpilib.TimedRobot):

	def robotInit(self):

		NetworkTables.initialize(server='roborio-5716-frc.local')

		#wpilib.CameraServer.launch('Vision.py:VisionOn')

		#self.Video = VideoRecorder()
		#wpilib.CameraServer.launch()


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

		#cannon

		self.motor_cannon_left = wpilib.Talon(5)
		self.motor_cannon_right = wpilib.Talon(6)

		#sucker

		self.sucker_motor = wpilib.Talon(7)

		#cannon pneumatics

		self.piston_cannon = wpilib.Solenoid(0,0)
		self.Compressor = wpilib.Compressor(0)
		self.PSV = self.Compressor.getPressureSwitchValue()

	def autonomousPeriodic(self):

		pass

	 
	def teleopPeriodic(self):

		# while True:
		# 	self.Video.VariablesInit()
		# 	self.Video.SmartColorRecognizer("green",(0,255,0),600, 3000)
		# 	self.Video.StartRecording()

		# 	key = cv2.waitKey(1)
		# 	if key == ord("q"):
		# 		break

		#Video.StopRecording()

		oi.read_control_inputs(state["Controller"])

		x = state["x_axis"]
		y = state["y_axis"]
		z = state["z_axis"]

		powerX = 0 if x < 0.20 and x > -0.20 else x
		powerY = 0 if y < 0.20 and y > -0.20 else y
		powerZ = 0 if z < 0.20 and z > -0.20 else z

		self.drive.driveCartesian(powerX * -0.7,powerY * 0.7, powerZ * -0.5, 0)

		#cannon

		self.motor_cannon_right.set(state["motor_cannon_activated"])
		self.motor_cannon_left.set(state["motor_cannon_activated"])

		self.piston_cannon.set(state["piston_activated"])

		#sucker

		self.sucker_motor.set(state["sucker_activated"])

		if self.PSV:
			self.Compressor.stop()
		else:
			self.Compressor.start()
		

if __name__ == '__main__':
	wpilib.run(MyRobot)
