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

#Add support for user prompt on launch to select between different APIs/Currencies
print "OPTIONS: BTC_mtgox, BTC_btce, BTC_bitstamp, DOGE_cryptsy"
input_var = input("Enter your choice (Case Sensitive): ")
print ("You entered: " + input_var)

def BTC_mtgox():
        mtgox = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
        if mtgox["result"] != "success":
                raise Exception("MtGox API failed!")
 
        current_price = mtgox["return"]["last"]["value"]

        #Prefix for display
        prefix = "BTC/USD: $"

        # > $1000 rollover, Rounds/Converts to int
        if (int(round(float(current_price))) > 1000):
                final_price = int(round(float(current_price)))
        else:
                final_price = current_price
        return final_price
        return prefix

def BTC_btce():
        btce = json.load(urllib2.urlopen('https://btc-e.com/api/2/btc_usd/ticker'))
        # No error handling response with btce API

        current_price = btce["ticker"]["last"]

        #Prefix for display
        prefix = "BTC/USD: $"

        # > $1000 rollover, Rounds/Converts to int
        if (int(round(float(current_price))) > 1000):
                final_price = int(round(float(current_price)))
        else:
                final_price = current_price
        return final_price
        return prefix

def BTC_bitstamp():
        btce = json.load(urllib2.urlopen('https://www.bitstamp.net/api/ticker/'))
        # No error handling response with bitstamp API

        current_price = btce["last"]

        #Prefix for display
        prefix = "BTC/USD: $"

        # > $1000 rollover, Rounds/Converts to int
        if (int(round(float(current_price))) > 1000):
                final_price = int(round(float(current_price)))
        else:
                final_price = current_price
        return final_price
        return prefix        

def DOGE_cryptsy():
        cryptsy = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
        if cryptsy["result"] != "1":
                raise Exception("Cryptsy API failed!")

        #Prefix for display
        prefix = "DOGE/BTC: "

        current_price = cryptsy["return"]["markets"]["DOGE"]["lasttradeprice"]
        # No rollover necessary, but need to figure out how to deal with decimal places
        return final_price
        return prefix

#Add support for switching between currencies by using button code
while 1:
        lcd.clear()
        #Calls function, gets time and formats.
        try:
                price = input_var()
        except Exception:
                lcd.message("API failed!")

        time = datetime.now().strftime( '%F %H:%M\n' )
        #Displays time on first line, BTC/USD rate on next line
        lcd.message(time)
        lcd.message(prefix + price)
        # Length of sleep between API call
        sleep(30)
