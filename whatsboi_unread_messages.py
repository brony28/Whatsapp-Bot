import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

options=webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/Mr. Nitin Tiwari/AppData/Local/Google/Chrome/User Data/Default')
options.add_argument('--profile-directory=Default')

chrome_browser=webdriver.Chrome(executable_path = '/Users/Mr. Nitin Tiwari/Downloads/chromedriver/chromedriver.exe', options=options)
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(15)

#only DMs and no group messages by checking mute icon.
unreadMsgs = chrome_browser.find_elements_by_xpath('//span[@class="_31gEB"]')

if not unreadMsgs:
    print("Total unread messages: 0")
else:
    print("Total unread messages: "+ str(len(unreadMsgs)))
    text = "Hi, I'm busy right now and will reply ASAP. BTW this is an automated message."
    for msg in unreadMsgs:
        msg.click()
        time.sleep(5)
        message_box=chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
        message_box.send_keys(text+Keys.ENTER)
        time.sleep(2)
       