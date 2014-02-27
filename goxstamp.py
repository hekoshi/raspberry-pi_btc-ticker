 #!/usr/bin/python
 
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import *
from time import sleep, strftime
from datetime import datetime
 
import json
import urllib2
import time

lcd = Adafruit_CharLCDPlate()
lcd.begin(16,1)
 
def GOX():
	mtgox = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
	current_price = mtgox["return"]["last"]["value"]
	# > $1000 rollover, Rounds/Converts to int
	if (int(round(float(current_price))) > 1000):
		gox_price = int(round(float(current_price)))
	else:
		gox_price = current_price
	return gox_price

def STAMP():
	stamp = json.load(urllib2.urlopen('https://www.bitstamp.net/api/ticker/'))
	current_price = stamp["last"]
	# > $1000 rollover, Rounds/Converts to int
	if (int(round(float(current_price))) > 1000):
		stamp_price = int(round(float(current_price)))
	else:
		stamp_price = current_price
	return stamp_price


while 1:
	lcd.backlight(lcd.GREEN)
	lcd.clear()
	#Calls BTC function, gets time and formats.
	gox = GOX()
	stamp = STAMP()
	time = datetime.now().strftime( '%F %H:%M\n' )
	#Displays time on first line, BTC/USD rate on next line.
	lcd.message(time)
	lcd.message( "$" + stamp + "||" "$" + gox)
	#Sleeps until next API call can be made. 
	sleep(30)
