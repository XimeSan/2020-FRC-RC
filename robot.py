
import wpilib
from wpilib.drive import MecanumDrive
import time
import oi
from state import state
from networktables import NetworkTables
import threading
import logging
import Camara2

# from cscore import CameraServer
# import navx


#from ICanSee import VideoRecorder
#import cv2
#import numpy as np
#Rasbperry Ip Adress: 10.57.16.87


class MyRobot(wpilib.TimedRobot):

	def robotInit(self):
		self.pop = Camara2.main()
		wpilib.CameraServer.launch()

		# NetworkTables.startClientTeam(5716)
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

		# self.chasis_controller = wpilib.Joystick(0)

		self.timer = wpilib.Timer()


		self.left_cannon_motor = wpilib.Talon(5)
		self.right_cannon_motor = wpilib.Talon(6)

		self.sucker = wpilib.Talon(7)

		self.front_left_motor = wpilib.Talon(3)
		self.rear_left_motor = wpilib.Talon(1)
		self.front_right_motor = wpilib.Talon(4)
		self.rear_right_motor = wpilib.Talon(2)

		self.front_left_motor.setInverted(True)

		self.color_wheel = wpilib.Talon(8)

		self.drive = MecanumDrive(
			self.front_left_motor,
			self.rear_left_motor,
			self.front_right_motor,
			self.rear_right_motor)

		#led
		self.green_led = wpilib.DigitalOutput(0)

		#cannon pneumatic
		self.Compressor = wpilib.Compressor(0)
		self.PSV = self.Compressor.getPressureSwitchValue()
		self.cannon_piston = wpilib.Solenoid(0,5)
		self.hook1 = wpilib.Solenoid(0,0) 
		self.hook2 = wpilib.Solenoid(0,7) 
		# self.navx = navx.AHRS.create_spi()
	def autonomousInit(self):

		self.timer.reset()
		self.timer.start()

	def autonomousPeriodic(self):

		position = self.pc.getString("Posicion", "Not jalando")

		print(position)

		wpilib.DriverStation.reportWarning(position,True)

		#state 1

		print(self.timer.get())
		if self.timer.get() < 9:
			self.cannon_piston.set(True)
		elif self.timer.get() >= 9 and self.timer.get() <= 10:
			self.right_cannon_motor.set(-1)
			self.left_cannon_motor.set(-1)
		elif self.timer.get() >= 10 and self.timer.get() < 13:
			self.cannon_piston.set(False)
		# elif state["timer.get()_auto"] >= 420 and state["timer.get()_auto"] < 520:
		# 	self.cannon_piston.set(True)
		# elif state["timer.get()_auto"] >= 520 and state["timer.get()_auto"] < 540:
		# 	self.cannon_piston.set(False)
		elif self.timer.get() >=  13 and self.timer.get() < 15:
			self.right_cannon_motor.set(0)
			self.left_cannon_motor.set(0)
			self.drive.driveCartesian(0, 0.5, 0, 0)
		elif self.timer.get() >= 15:
			self.drive.driveCartesian(0, 0, 0, 0)
			self.right_cannon_motor.set(0)		
			self.left_cannon_motor.set(0)

			self.timer.stop()
			
			

		# time.sleep(3)
		# elif state["timer_auto"] > 40 and state["timer_auto"] <= 80: 
		# 	self.cannon_piston.set(False)
		# # time.sleep(0.7)
		# elif state["timer_auto"] > 80 and state["timer_auto"] <= 150:
		# 	self.cannon_piston.set(True)
		# 	self.sucker.set(1)
		# # time.sleep(4)
		# # self.drive.driveCartesian(0, 0, 0) 
		# elif state["timer_auto"] > 150 and state["timer_auto"] < 250:
		# 	self.front_left_motor.set(-1)
		# 	self.rear_left_motor.set(-1)
		# 	self.front_right_motor.set(-1)
		# 	self.rear_right_motor.set(-1)
		# 	state["timer_auto"] == 0
		# # time.sleep(5)

		#



#-----------------------------------------------------------------------------------------------------------

	def teleopPeriodic(self):

		wpilib.CameraServer.launch('vision.py:main')

		# self.pc = NetworkTables.getTable("Posicion")

		oi.ReadControllerInputs()

		x = state["x_axis"]
		y = state["y_axis"]
		z = state["z_axis"]

		powerX = 0 if x < 0.20 and x > -0.20 else x
		powerY = 0 if y < 0.20 and y > -0.20 else y
		powerZ = 0 if z < 0.20 and z > -0.20 else z

		self.drive.driveCartesian(powerX * -0.9,powerY * 0.9, powerZ * -0.9, 0)
#----------------------------------------------------------------------------------------------------------
		if state["cannon"] > 0.7:
			self.right_cannon_motor.set(-1)
			self.left_cannon_motor.set(-1)
		else:
			self.right_cannon_motor.set(0)
			self.left_cannon_motor.set(0)

		# if state["sucker_manual"]:
		# 	self.sucker.set(0.6)
		# elif state["sucker_manual"] == False:
		# 	self.sucker.set(0)

		# self.cannon_piston.set(state["piston_cannon"])
#------------------------------------------------------------------------------------------------------------
#Modificaciones para el gancho 10/2/2020	
		if state["hook"] == True and state["hook_status"] == False:
			state["hook_status"] = True
			state["solenoid_status"] = True
			time.sleep(.3)
		elif state["hook"] == True and state["hook_status"] == True:
			state["hook_status"] = False
			time.sleep(.3)
			state["solenoid_status"] = True
		if state["solenoid_status"] == True:

			if state["hook_status"] == True:
				self.hook1.set(True)
				self.hook2.set(False)
			else:
				self.hook1.set(False)
				self.hook2.set(True)
		else:
			self.hook1.set(True)
			self.hook2.set(True)


#----------------------------------Semi automatico, cannon de rutina---------------------------------------------------
		#cannon rutine		
		# if state["cannon2"]:
		# 	#enciende los motores del cañón
		# 	self.right_cannon_motor.set(-1)
		# 	self.left_cannon_motor.set(1)
		# 	#ocupas el for para que repita los pistones 5 veces
		# 	i = 0
		# 	for i in range(0,5):
		# 		#enciende el piston
		# 		state["auto_piston"] = True
		# 		self.cannon_piston.set(state["auto_piston"])
		# 		#espera 1 segundo
		# 		time.sleep(1)
		# 		#apaga el piston
		# 		state["auto_piston"] = False
		# 		self.cannon_piston.set(state["auto_piston"])
		# 		#espera un segundo antes de repetir la rutina
		# 		time.sleep(1)
		# 	#acabando la rutina apaga los motores
		# 	self.right_cannon_motor.set(0)
		# 	self.left_cannon_motor.set(0)
		# 	state["auto_piston"] = False
		# 	self.cannon_piston.set(state["auto_piston"])

#------------------------------------Manual cannon motores-----------------------------------------------------
		# if state["cannon"] == True and state["cannon_status"] == False:
		# 	state["cannon_status"] = True
		# 	time.sleep(.1)
		# elif state["cannon"] == True and state["cannon_status"] == True:
		#  	state["cannon_status"] = False
		#  	time.sleep(.1)
		# if state["cannon_status"] == True:
		#  	self.right_cannon_motor.set(-1)
		#  	self.left_cannon_motor.set(-1)
		# else:
		#  	self.right_cannon_motor.set(0)
		#  	self.left_cannon_motor.set(0)
#------------------------------------Manual Sucker-----------------------------------------------------
		# if state["sucker"] == True and state["sucker_status"] == False:
		# 	state["sucker_status"] = True
		# 	time.sleep(.3)
		# elif state["sucker"] == True and state["sucker_status"] == True:
		# 	state["sucker_status"] = False
		# 	time.sleep(.3)
		if state["sucker"]:
			self.sucker.set(1)
#-------------------------------------Reverse Sucker Provisional------------------------------------------------------	
		elif state["reverse_sucker"]:
			self.sucker.set(-1)
		else:
			self.sucker.set(0)
#-------------------------------------Manual cannon piston------------------------------------------------------	
		if state["piston_cannon"] > 0.7:
		 	self.cannon_piston.set(False)
		else:
		 	self.cannon_piston.set(True)
#---------------------------------------------------------------------------------------------------------------
		# if state["cannon"]:
		# 	self.right_cannon_motor.set(-1)
		# 	self.left_cannon_motor.set(1)
		# else:
		# 	self.right_cannon_motor.set(0)
		# 	self.left_cannon_motor.set(0)

		# if state["sucker"]:
		# 	self.sucker.set(1)
		# else:
		# 	self.sucker.set(0)
#---------------------------------------------------------------------------------------------------------------
		if state["aling"]:
			print("jalo")
			self.green_led.set(0)
			if state["target_position"] != "Not Jalando" or "":
				print("Jalando")

				if state["target_position"] == "Top Left":
					self.drive.driveCartesian(-0.5, 0, 0)
				elif state["target_position"] == "Top Right":
					self.drive.driveCartesian(0.5, 0, 0)
				elif state["target_position"] == "Top Center":
					self.drive.driveCartesian(0, 0, 0)
					print("Shoot!")

			else:

				self.drive.driveCartesian(0, 0, 0)
				print("Not detection!")

		else:

			# print("No jalo")

			self.green_led.set(1)

		# if state["navxon"]:
		# 	print("Angle: " + self.navx.getAngle())
	
#-----------------------------------------------------------------------------------------------
		if state["color_wheel"]:
			if state["color_wheel_2"]:

				self.color_wheel.set(-0.2)
				wpilib.wait(0.2)
			else:
				self.color_wheel.set(1)
		else:
			self.color_wheel.set(0)



		if self.PSV:
			self.Compressor.stop()

		else:
			self.Compressor.start()


if __name__ == '__main__':
	wpilib.run(MyRobot)
