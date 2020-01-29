from state import state
import wpilib 


def read_control_inputs(control_type):

	if control_type == "PacificRim":

		read_chasis_inputs(0)
		read_abilities_inputs(1)

	elif control_type == "Chasis" or control_type == "Piko":

		read_abilities_inputs(0)
		read_chasis_inputs(0)

	else:

		print ("Non-existent control type")
		wpilib.DriverStation.reportWarning(str("Non-existent control type"),True)

def read_chasis_inputs(control_port):

	chasis_controller = wpilib.Joystick(control_port)

	state["x_axis"] = chasis_controller.getRawAxis(0)
	state["y_axis"] = chasis_controller.getRawAxis(1)
	state["z_axis"] = chasis_controller.getRawAxis(4)

def read_abilities_inputs(control_port):

	abilities_controller = wpilib.Joystick(control_port)

	#cannon
	
	cannon_motor = abilities_controller.getRawAxis(5)

	sucker = abilities_controller.getRawButton(1)

	turn_cannon_piston = abilities_controller.getRawButton(6)

	if cannon_motor == 1:

		if state["eje_t_state"] == False:

			state["motor_cannon_activated"] = 0.7
			state["eje_t_state"] = True

		else:

			state["motor_cannon_activated"] = 0
			state["eje_t_state"] = False

	if sucker:

		if state["left_shoulder_state"] == False:

			state["sucker_activated"] = 0.7
			state["left_shoulder_state"] = True

		else:
			state["sucker_activated"] = 0
			state["left_shoulder_state"] = False

	if turn_cannon_piston:

		if state["right_shoulder_state"] == False:

			state["piston_activated"] = True
			state["right_shoulder_state"] = True

		else:
			state["piston_activated"] = False
			state["right_shoulder_state"] = False




