Raspberry-Pi-BTC-Ticker
=======================
##What is this?
This is a python script designed to run on a Raspberry pi, and display the current Bitcoin/USD exchange rate on an attached LCD screen. This saves time and allows for at a glance viewing. Support is being added for more cryptocoins.

UPDATE 2014-02-28: Currently, the code is a little messy, and will be refactored in the coming days. Stay tuned!
	
####Background
I got tired of pulling up my browser and navigating to a graphing site everytime I wanted to check the BTC/USD rate. There had to be be a better solution. I tried some browser addons but they were clunky and took up precious screen space, then I realized an external LCD would be perfect for displaying this kind of information. I ordered a [16x2 RGB LCD kit from Adafruit.com](http://www.adafruit.com/products/1109), soldered it together (Look at those sexy solder joints!), then wrote some python code for my Raspberry Pi that polls the MtGox API every 30s (Limit with standard API), and displays it on the screen in the format shown below:

	| YYYY-MM-DD HH:MM |
	| BTC/USD: $XXX.XX |

####Shameless donation address
If this script helped you out or inspired you, I'll gladly accept a few of your mBTC :). Donations will encourage me to work on this more, write razor sharp code, and develop cool new features.           
**1MJDPZFEFA8tEzDb2gFdU6RSRVHfGGh9Ad**

####Status
I would like to release version 1.0 in the near future, once more features are implimented and the performance and error handling is tested. I plan on including more thorough documentation as well as templates for adding new API feeds.

####Variations
1. **bitcointicker.py**                        
Original script, BTC/USD, and allows for multiple exchange switching.
2. **goxstamp.py**                          
Script used to compare the price of Bitstamp/Goxcoin, during the gox solvency crisis.
3. **veryworkingmuchshibe.py**                              
DOGE specific script relying on the cryptsy api, created in response to an issue raised.

####Ideas for future expansion:            
	 [] Change display color based on market uptick/downtick.                   
	 [] Dimming backlight during certain timeslots (While the human is sleeping)          
	 [] Recovery from dropped wireless connection / API call failure.
	 [] Switching between BTC and mBTC. (Manual at first)
	 [] Support for LTC + DOGE + altcoin price tickers (Controllable by button press)         
	 [] Sound notification based on adjustable thresholds.
	 [] EMA 10/21 strategy notification.
	 [] Change RGB LCD to a VFD display to reduce glare/light pollution.  

####Psychological Effects
Aside from getting woken up by an alien blue glow at 3AM, and seeing the exchange rate on my desk all the time, surprisingly little has changed. Knowing the exact rate is useful when trading, but I find the data is difficult to remember, so I can see the use for a 1hr/24hr averaging system, and having the backlight change from green/red on uptick/downtick.

Will report back if I experience a singularity with the blockchain.

####Photos
Initial Picture
![FirstPicture](http://i.imgur.com/W5mvL72.jpg)                 
Picture demonstrating goxstamp.py during the gox crisis.
![SecondPicture](http://i.imgur.com/pChEKp1.jpg)

