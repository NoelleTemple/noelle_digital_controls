#sample code

#this package should already be included with Raspbian
import RPi.GPIO as GPIO
import time
#This is the setup we are testing with the sample
from servocntl_pkg import servo

#initialize the servo motor with a description, the pin number on the board (not the GPIO number
#and the frequency at which the PWM signal should run (50Hz is average)
test=servo(description="testing control of Servo", boardpin = 35, frequency = 50)
#this will print out all the information that you have set
test.getinfo()

test.setup()

test.moveservo()
