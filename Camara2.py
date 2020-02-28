from cscore import CameraServer, UsbCamera
def main():

	cs = CameraServer.getInstance()
	cs.enablelogging()

	usb1= cs.startAutomaticCapture(dev=0)
	usb2= cs.startAutomaticCapture(dev=1)

	cs.waitForever()

if __name__=="__main__":
	import logging
	logging.basicConfig(level=logging.DEBUG)
	import networtables
	networktables.initialize(server="10.57.16.2")

