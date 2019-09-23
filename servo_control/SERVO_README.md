#SERVO CONTROL

If you have not cloned this repo yet:
```
cd ~
git clone https://github.com/NoelleTemple/noelle_digital_controls.git
cd /noelle_digital_controls/servo_control
```
If you have cloned this repo:
```
cd ~/noelle_digital_controls/servo_control
```

To use the sample code, set up a servo motor connecting the control signal to pin 35, ground to pin 39, and Vcc to pin 17.

Raspberry Pi Pinout:
https://learn.sparkfun.com/tutorials/raspberry-gpio/gpio-pinout

![Raspberry Pi Pinout](https://github.com/NoelleTemple/noelle_digital_controls/blob/master/picture/RPi_Pinout.jpg)


Example Servo:
https://components101.com/servo-motor-basics-pinout-datasheet

![Servo Pinout](https://github.com/NoelleTemple/noelle_digital_controls/blob/master/picture/ServoPinout.png)

Make sure to install the package:
```
sudo pip install servo_control/
```
This will automatically find the setup.py file and install the package.

Navigate to Sample code:
```
cd ~/noelle_digital_controls/servo_control/test
```
Run Sample code:
```
python sample.py
```
Here, the servo is identified with a desciption, the pin number on the board, and the frequency at which the control signal will opporate.  In this code, the servo will move to 4 different positions, changing based on the duty cycle of the control signal.

This contains the GPIO package, that comes pre-installed with Raspbian.  
For more on GPIO uses:
```
https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
https://projects.raspberrypi.org/en/projects/grandpa-scarer/4
```

To find the file describing the class:
```
cd ~/noelle_digital_controls/servo_control/servocntl_pkg/
nano servo.py
```
Here, the description of the servo, the pin number on the board, and the frequency at which the PWM signal operates is initialized.  
