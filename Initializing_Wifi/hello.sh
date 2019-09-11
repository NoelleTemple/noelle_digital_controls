#!/bin/bash

#get Private IP Address
export IPAddr=`hostname -I`
#Message (no spaces) to send to broker
export StrtRpt="Private_IP:$IPAddr"
#command to publish message to broker
cmd=`mosquitto_pub -h <hostname> -u <username> -p <portnumber> -P <password> -t <topic> -m $StrtRpt`


