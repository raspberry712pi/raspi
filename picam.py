from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()  


sleep(2)  
camera.capture('/home/pi/Desktop/image.jpg')  
print("Photo captured!")

camera.start_recording('/home/pi/Desktop/video.h264')  
sleep(10)  
camera.stop_recording()  
print("Video recorded!")

camera.stop_preview()  
