import wpilib
from wpilib.drive import MecanumDrive
import time
import oi
from state import state
from networktables import NetworkTables
#from ICanSee import VideoRecorder
#import cv2

class MyRobot(wpilib.TimedRobot):

	def robotInit(self):

		NetworkTables.initialize(server='roborio-5716-frc.local')

		#wpilib.CameraServer.launch('Vision.py:VisionOn')

		#self.Video = VideoRecorder()
		#wpilib.CameraServer.launch()

		self.chasis_controller = wpilib.Joystick(0)

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

		#cannon and sucker

		self.cannon_motor_right = wpilib.Talon(4)
		self.cannon_motor_left = wpilib.Talon(5)
		self.sucker_motor = wpilib.Talon(6)

		#cannon pneumatic
		self.Compressor = wpilib.Compressor(0)
		self.PSV = self.Compressor.getPressureSwitchValue()
		self.cannon_piston = wpilib.Solenoid(0,0)


	def autonomousPeriodic(self):

		pass

	 
	def teleopPeriodic(self):

		oi.ReadControllerInputs()

		x = state["x_axis"]
		y = state["y_axis"]
		z = state["z_axis"]

		powerX = 0 if x < 0.20 and x > -0.20 else x
		powerY = 0 if y < 0.20 and y > -0.20 else y
		powerZ = 0 if z < 0.20 and z > -0.20 else z

		self.drive.driveCartesian(powerX * -0.7,powerY * 0.7, powerZ * -0.5, 0)

	
		#pneumatics cannon

		self.cannon_piston.set(state["cannon_piston_activated"])

		if self.PSV:
			self.Compressor.stop()
		else:
			self.Compressor.start()


if __name__ == '__main__':
	wpilib.run(MyRobot)
