from time import sleep
from pygame import mixer
import RPi.GPIO as GPIO

var=1
counter = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.OUT)
def playMp3() :
	mixer.init()
	mixer.music.load('/usr/share/scratch/Media/Sounds/Animal/Cat.mp3')
	mixer.music.play()

def getTime() :
	GPIO.output(7,True)
		

def turnOn7() :
	GPIO.output(7,True)
	
def turnOff7() :
	GPIO.output(7,False)

def my_callback(channel):
    if var == 1:
        sleep(1.5)  # confirm the movement by waiting 1.5 sec 
        if GPIO.input(5): # and check again the input
            print("Movement!")
            turnOn7()
            # stop detection for 20 sec
            GPIO.remove_event_detect(5)
	    sleep(5)
	    turnOff7()
            GPIO.add_event_detect(5, GPIO.RISING, callback=my_callback, bouncetime=300)

GPIO.add_event_detect(5, GPIO.RISING, callback=my_callback, bouncetime=300)

# you can continue doing other stuff here
while True:
#	playMp3()
	sleep(10)
    	pass
