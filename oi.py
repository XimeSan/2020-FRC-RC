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

	# state["cannon"]	= gun_controller.getRawAxis(3)
	# state["sucker"]	= gun_controller.getRawAxis(2)







	
