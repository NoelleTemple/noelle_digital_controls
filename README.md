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

-Insert SD card to Raspberry Pi, and connect R-Pi to monitor (HDMI), keyboard (USB), and mouse (USB)
 
 -
