import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def my_callback(channel):
	print "rising edge detected on 21"

GPIO.add_event_detect(21, GPIO.RISING, callback=my_callback, bouncetime=300)

while 1:
	try:
		print GPIO.input(21)
		#GPIO.wait_for_edge(21, GPIO.FALLING)
	except KetboardInterrupt:
		GPIO.cleanup()	#clean up on GPIO on CNTL+C exit

	time.sleep(10)

GPIO.cleanup()

