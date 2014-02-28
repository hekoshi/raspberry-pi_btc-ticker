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

def DOGE():
        cryptsy = json.load(urllib2.urlopen('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132'))
        #if cryptsy["success"] != "1":
        #                raise Exception("Cryptsy API failed!")
        current_price = cryptsy["return"]["markets"]["DOGE"]["lasttradeprice"]
        # No rollover necessary, but need to figure out how to deal with decimal places
        return current_price

#Add support for switching between currencies by using button code
while 1:
        lcd.clear()
        #Calls BTC function, gets time and formats
        price = DOGE()
        time = datetime.now().strftime( '%F %H:%M\n' )
        #Displays time on first line, BTC/USD rate on next line
        lcd.message(time)
        lcd.message( "DOGE: " + price)
        #Sleeps until next API call is possible
        #Needs to be customized per API, add support next
        sleep(30)


