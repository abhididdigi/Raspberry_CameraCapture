import picamera
import random
import string
import os

random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10));
camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True
image_name = "images/"+"ashimg_"+random_string+".jpg";
camera.capture(image_name)
os.system("Yes y | gdrive_sync sync-up AMMU images/")
