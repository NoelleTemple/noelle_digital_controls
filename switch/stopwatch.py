from Adafruit_LED_Backpack import SevenSegment
import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

segment = SevenSegment.SevenSegment(address=0x70)
segment.begin()
push=False
cnt=0

def my_callback(channel):
	global push, cnt
	print "rising edge detected on 21"
	if (push==False):
		push=True
		cnt = 0
	else:
		push=False



GPIO.add_event_detect(21, GPIO.RISING, callback=my_callback, bouncetime=300)
while 1:
	print("start")
	segment.clear()
	if (push==True):
		cnt=cnt+1
		segment.set_digit(0, int(cnt/1000))
		segment.set_digit(1, int(cnt/100))
		segment.set_digit(2, int(cnt/10))
		segment.set_digit(3, int(cnt%10))
	else:
		segment.set_digit(0, int(cnt/1000))
		segment.set_digit(1, int(cnt/100))
		segment.set_digit(2, int(cnt/10))
		segment.set_digit(3, int(cnt%10))
	time.sleep(1)
	segment.write_display()

GPIO.cleanup()

