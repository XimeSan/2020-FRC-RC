from state import state
import wpilib


def ReadControllerInputs():

	chasis_controller = wpilib.Joystick(0)



	gun_controller = wpilib.Joystick(1)

	state["x_axis"] = chasis_controller.getRawAxis(0)
	state["y_axis"] = chasis_controller.getRawAxis(1)
	state["z_axis"] = chasis_controller.getRawAxis(4)

	state["sucker"] = gun_controller.getRawButton(2)
	state["cannon"] = gun_controller.getRawButton(1)
	state["hook"] = gun_controller.getRawButton(3)
	state["piston_cannon"] = gun_controller.getRawButton(6)
	state["cannon2"] = gun_controller.getRawButton(4)
	state["piston_cannon_fire"] = gun_controller.getRawButton(7)

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







	
