from state import state
import wpilib 

def ReadControllerInputs():

	chasis_controller = wpilib.Joystick(0)
	abilities_controller = wpilib.Joystick(1)

	state["x_axis"] = chasis_controller.getX()
	state["y_axis"] = chasis_controller.getY()
	state["z_axis"] = chasis_controller.getRawAxis(4)


