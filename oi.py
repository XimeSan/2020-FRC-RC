from state import state
import wpilib


def ReadControllerInputs():

	chasis_controller = wpilib.Joystick(0)

	state["x_axis"] = chasis_controller.getRawAxis(0)
	state["y_axis"] = chasis_controller.getRawAxis(1)
	state["z_axis"] = chasis_controller.getRawAxis(4)






	
