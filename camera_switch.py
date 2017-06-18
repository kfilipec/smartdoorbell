import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BOARD)

pin = 8

GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD.UP)

i=0

try:

while True:
    input_state = GPIO.input(pin)
    if input_state == False:
        subprocess.call("fswebcam -d /dev/video0 -r 1024x768 -S0 "+str(i)+"pic.jpg",shell=True) print('PIC CAPTURED')
        i=i+1
        time.sleep(0.2)
        
    if input_state == True:
          time.sleep(0.2)

GPIO.cleanup()
          
        
