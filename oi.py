from state import state
import wpilib


def ReadControllerInputs():

	chasis_controller = wpilib.Joystick(0)



	gun_controller = wpilib.Joystick(1)

	state["x_axis"] = chasis_controller.getRawAxis(4)
	state["y_axis"] = chasis_controller.getRawAxis(1)
	state["z_axis"] = chasis_controller.getRawAxis(0)
	state["aling"] = chasis_controller.getRawButton(1)

	state["sucker"] = gun_controller.getRawButton(1)
	state["cannon"] = gun_controller.getRawAxis(2)
	state["hook"] = gun_controller.getRawButton(4)
	state["piston_cannon"] = gun_controller.getRawAxis(3)
	state["cannon2"] = gun_controller.getRawButton(8)
	state["color_wheel"] = gun_controller.getRawButton(5)
	state["color_wheel_2"] = gun_controller.getRawButton(6)
	state["reverse_sucker"] = gun_controller.getRawButton(2)
	#state["reverse_sucker"] = gun_controller.getRawButton(2)

#Xbox 360 button bind
#A=1
#B=2
#X=3
#Y=4
#5=LB
#6=RB
#7=Back
#8=start
#L=9
#R=10
#LT=Axis 4
#RT=Axis 5


	# state["cannon"]	= gun_controller.getRawAxis(3)
	# state["sucker"]	= gun_controller.getRawAxis(2)







	
