import selenium
from selenium import webdriver
import time
bank = 0
run = True

#locate user firefox profile settings and launch the browser with them
def launchbrowserwithsettings():
	options = webdriver.FirefoxOptions()
	options.profile = webdriver.FirefoxProfile("/home/kali/.mozilla/firefox/********.default-esr") #Replace ********.default-esr with your firefox profile on your own machine
	driver = webdriver.Firefox(options=options) # assign your profile to driver
	return driver 
def makedamoney():
	driver = launchbrowserwithsettings()
	driver.get("https://stake.us/?tab=dailyBonus&currency=btc&modal=wallet") #open browser and go to link
	time.sleep(120) #wait for browser to load
	claimbutton= driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/form/button") #find and assign button to a variable
	claimbutton.click() #click the button to make da money
	print("$Dollar Collected$" + "\nYou now have $" + str(bank))
	time.sleep(120) # wait to ensure colleciton
	driver.close() # close the browser

while (run):
	time.sleep(86580) # wait 24 hours and 30 mins for button to respawn
	makedamoney()
	bank += 1

