import cv2
import numpy
import time

video = cv2.VideoCapture(1)

green_lower = numpy.array([38,70,15], numpy.uint8)
green_upper = numpy.array([73,255,255], numpy.uint8)


def VisionOn():

	check,frame = video.read(0)

	HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	green = cv2.inRange(HSV, green_lower, green_upper)

#	cv2.imshow("Color Tracking",frame)


	color_data = "green"
	color = "green"

	hexagon_status = ""

	width = video.get(3)
	height = video.get(4)

	# Divides videos width and height into 3, to create the quadrants

	q_width = width/3
	q_height = height/3

	#green_color_range


	# Lrectangle = cv2.rectangle(frame, (0,720), (426,0), (0,255,0), 1)
	# Mrectangle = cv2.rectangle(frame, (426,720), (852,0), (0,255,0), 1)
	# Rrectangle = cv2.rectangle(frame, (852,720), (1280,0), (0,255,0), 1)

	# Urectangle = cv2.rectangle(frame, (0,240), (1280,0), (0,255,0), 1)
	# MMrectangle = cv2.rectangle(frame, (0,480), (1280,241), (0,255,0), 1)
	# Drectangle = cv2.rectangle(frame, (0,720), (1280,480), (0,255,0), 1)

	# print (check)
	# print (frame)
	# blur = cv2.GaussianBlur(frame ,(5,5), 0)
	# image = cv2.Canny(blur,50,150)


	if color == "red":
		color_data = red
	elif color == "blue":
		color_data = blue
	elif color == "yellow":
		color_data = yellow
	elif color == "green":
		color_data = green
	elif color == "orange":
		color_data = orange
	elif color == "black":
		color_data = black
	elif color == "white":
		color_data = white

	(contours,hierarchy) = cv2.findContours(color_data, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for pic, countour in enumerate(contours):
		area = cv2.contourArea(countour)
		if area > 500:
			x,y,w,h = cv2.boundingRect(countour)
			box = cv2.rectangle(frame, (x,y), (x+w, y+h),([0,255,0]) ,2)
			cv2.putText(box, color, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, ([0,255,0]))
			if color == "green":
				approx = cv2.approxPolyDP(countour,0.01*cv2.arcLength(countour,True),True)
				if len(approx) == 6:
					cv2.putText(frame, "Distance: " + str(area), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
					ObjectWidth = w + x 
					ObjectHeight = y + h
				
				# ObjectHeight = 
				# height/3 = 240 
				# width/3 = 426 
				
				# determines the position of the given shape
				
					if ObjectWidth < q_width and ObjectHeight > (q_height)*2:
						hexagon_status = "Bottom Left"
					elif ObjectWidth < q_width and ObjectHeight < (q_height)*2 and ObjectHeight > q_height:
						hexagon_status = "Middle Left"
					elif ObjectWidth < q_width and ObjectHeight < q_height:
						hexagon_status = "Top Left"
					elif ObjectWidth > (q_width)*2 and ObjectHeight > (q_height)*2:
						hexagon_status = "Bottom Right"
					elif ObjectWidth > (q_width)*2 and ObjectHeight < (q_height)*2 and ObjectHeight > q_height:
						hexagon_status = "Middle Right"
					elif ObjectWidth > (q_width)*2 and ObjectHeight < q_height:
						hexagon_status = "Top Right"
					elif ObjectWidth < (q_width)*2 and ObjectWidth > q_width and ObjectHeight < q_height:
						hexagon_status = "Top Middle"
					elif ObjectWidth < (q_width)*2 and ObjectWidth > q_width and ObjectHeight > (q_height)*2:
						hexagon_status = "Bottom Middle"
					else:
						hexagon_status = "Centered"
			else:
				pass


def StopRecording():

	video.release()
	cv2.destroyAllWindows()

while True:
	VisionOn()

	key = cv2.waitKey(1)
	if key == ord("q"):
		break

		StopRecording()