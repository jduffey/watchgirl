#!/bin/sh
# launcher.sh
# Instructions for running on RaspberryPi:
# command: sudo chmod 755 launcher.sh
# command: crontab -e
# add the following line:
# @reboot sleep 15 && sh /home/pi/watchgirl/launcher.sh


cd /
cd home/pi/watchgirl
sudo python3 standard_unicorn_signalmaker.py
cd /
