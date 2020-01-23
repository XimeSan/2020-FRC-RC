import wpilib
from wpilib.drive import MecanumDrive
import time
from state import state
import oi

# import navx

class MyRobot(wpilib.TimedRobot):

	def robotInit(self):

		self.chasis_controller = wpilib.Joystick(0)


		self.front_left_motor = wpilib.Talon(0)
		self.rear_left_motor = wpilib.Talon(1)
		self.front_right_motor = wpilib.Talon(2)
		self.rear_right_motor = wpilib.Talon(3)



		self.drive = MecanumDrive(
			self.front_left_motor,
			self.rear_left_motor,
			self.front_right_motor,
			self.rear_right_motor)

		#gyro

		# self.navx = navx.AHRS.create_spi()
		# self.analog = wplib.AnalogInput(navx.getNavxAnalogInChannel(0))

		#cannon

		self.cannon_motor_right = wpilib.Talon(4)
		self.cannon_motor_left = wpilib.Talon(5)

		#cannon pneumatic
		self.Compressor = wpilib.Compressor(0)
		self.PSV = self.Compressor.getPressureSwitchValue()
		self.cannon_piston = wpilib.Solenoid(0,0)

	# def disabled(self):
	# 	self.logger.info("Entered disabled mode")

	# 	self.timer.reset()
	# 	self.timer.start() 

	# 	while self.isDisabled():
	# 		if self.timer.hasPeriodPassed(0.5):
	# 			self.sd.putBoolean(
	# 			 	"SupportsDisplacement" , self.navx._isDisplacementSupported()
	# 			 	)
	# 			self.sd.putBoolean("IsCalibrating", self.navx.isCalibrating())
	# 			self.sd.putBoolean("IsConnected", self.navx.isConnected())
	# 			self.sd.putNumber("Angle", self.navx.getAngle())
	# 			self.sd.putNumber("Pitch", self.navx.getPitch())
	# 			self.sd.putNumber("Yaw", self.navx.getYaw())
	# 			self.sd.putNumber("Roll", self.navx.getRoll())
	# 			self.sd.putNumber("Analog", self.navx.getVoltage())
	# 			self.sd.putNumber("Timestamp", self.navx.getLastSensorTimestamp())

			

	# 		wpilib.Timer.delay(0.010)


	def autonomousPeriodic(self):

		pass

	 
	def teleopPeriodic(self):

		oi.read_control_inputs(state["Controller"])
		
		self.x = self.chasis_controller.getX()
		self.y = self.chasis_controller.getY()
		self.z = self.chasis_controller.getRawAxis(4)

		x = self.x 
		y = self.y 
		z = self.z

		powerX = 0 if x < 0.10 and x > -0.10 else x
		powerY = 0 if y < 0.10 and y > -0.10 else y
		powerZ = 0 if z < 0.10 and z > -0.10 else z

		self.drive.driveCartesian(powerX * 0.6,-powerY * 0.6, powerZ * 0.5, 0)

		# if self.navx.getAngle() == 90:
		# 		print("90°")

		#cannon

		self.cannon_motor_right.set(state["cannon_motor_activated"])
		self.cannon_motor_left.set(state["cannon_motor_activated"]*-1)

		#pneumatics cannon

		abilities_controller = wpilib.Joystick(0)

	#cannon


		self.cannon_piston.set(state["cannon_piston_activated"])

		if self.PSV:
			self.Compressor.stop()
		else:
			self.Compressor.start()


if __name__ == '__main__':
	wpilib.run(MyRobot)
