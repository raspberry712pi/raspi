from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()	#start camera
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')	# take a picture
camera.stop_preview()	# stop camera

