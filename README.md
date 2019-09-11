# noelle_digital_controls

Please do not delete these instructions.

-Download Rasbian Buster with desktop and recommended software.
  ```
  https://www.raspberrypi.org/downloads/raspbian/
  ```
-Download Etcher
  ```
  https://www.balena.io/etcher/
  ```
-Flash SD card using Etcher software and Rasbian image.

-Edit wpa_supplicant.conf file to include proper credentials for WIFI 
  # ADD THIS SCRIPT
  
  To get hash code for password:
  ```
  echo -n "password" | iconv -t UTF-16LE | openssl md4
  ```
  If using multiple networks, assign priority.

-Add wpa_supplicant.conf file to boot directory on SD card.

-Add interfaces file to boot directory on SD card.
  # ADD THIS SCRIPT

-Insert SD card to Raspberry Pi, and connect R-Pi to power supply (micro USB), monitor (HDMI), keyboard (USB), and mouse (USB)
 
-In R-Pi terminal


-Check to make sure interfaces is in this file path:
```
/etc/network/
```
  if not, navigate to directory with interfaces file (/boot) 
  ```
  sudo cp interfaces /etc/network
  ```
  and restart R-Pi
  
-Check to make sure wpa_supplicant.conf is in in this file path:
```
/etc/wpa_supplicant....
```
-In R-Pi terminal

```
sudo raspi-config
```
  -Enable ssh
  -Enable i2c
  -Enable spi
  -Enable serial

-In R-Pi terminal
```
ifconfig
```
  Note IP address of R-Pi

-In separate terminal
```
ssh pi@<IP Address>
```
  can remove monitor, mouse, and keyboard from R-Pi here, because we can access it from separate machine.  Do not turn it off yet.

-In new VM terminal
  navigate to hello.sh
  can download here
  # Add file

-In VM terminal
  ```
  scp hello.sh pi@<IP Address>:/home/pi
  ```

-In VM terminal 
  navigate to ip_boot.service
  can download here
  # Add file

-In VM terminal 
  ```
  scp ip_boot.service pi@<IP Address>:/home/pi
  ```
  
-In R-Pi terminal (ssh)
  ```
  cd /home/pi/
  ```
  ```
  sudo mv ip_boot.service /etc/systemd/system/ip_boot.service
  ```
  ```
  cd /etc/systemd/system
  ```
  ```
  sudo systemctl enable ip_boot.service
  ```
  It may ask you to run another command using daemon.  If it does, run the suggested command.
-
  
