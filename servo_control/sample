#sample code

#this package should already be included with Raspbian
import RPi.GPIO as GPIO
import time
#This is the setup we are testing with the sample
from Servo import Servo

#initialize the servo motor with a description, the pin number on the board (not the GPIO number
#and the frequency at which the PWM signal should run (50Hz is average)
test=Servo(description="testing control of Servo", boardpin = 35, frequency = 50)
#this will print out all the information that you have set
test.getinfo()

#keeps warnings from stopping the execution of the code
GPIO.setwarnings(False)
#Sets the pin number supplied to be the pin number on the board, and not the GPIO number. 
#For GPIO number, use GPIO.BCM
GPIO.setmode(GPIO.BOARD)

#Set the pin to an output
GPIO.setup(test.boardpin,GPIO.OUT)
#set up pulse width modulation and the frequency for the signal on the pin
p=GPIO.PWM(test.boardpin,test.frequency)

#start PWM signal
p.start(0)

#Change duty cycle to change the position of the servo motor
p.ChangeDutyCycle(7.5)
time.sleep(2)
p.ChangeDutyCycle(12.5)
time.sleep(2)
p.ChangeDutyCycle(7.5)
time.sleep(2)
p.ChangeDutyCycle(2.5)
time.sleep(2)

#stop
p.stop()
#clear pins
GPIO.cleanup()

