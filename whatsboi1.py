import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import schedule


def new_chat(user_name):
	time.sleep(2)
	new_chat = chrome_browser.find_element_by_xpath('//div[@class="_3qx7_"]')
	new_chat.click()

	new_user = chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
	new_user.send_keys(user_name)
	time.sleep(2) 

	try:
		user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
		user.click()
	except NoSuchElementException: 
		print('Given user "{}" not found in the contact list'.format(user_name))
	except Exception as e:
		chrome_browser.close()
		#print(e)
		sys.exit()

def send_message():
	message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
	message_box.send_keys('Hi, I am WhatsApp bot. This is a scheduled message at {}'.format(scheduled_time)+Keys.ENTER)


if __name__=='__main__':
	options=webdriver.ChromeOptions()
	options.add_argument('--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data/Default')
	options.add_argument('--profile-directory=Default')

	chrome_browser=webdriver.Chrome(executable_path = 'C:/Users/user/Downloads/chromedriver.exe', options=options)
	chrome_browser.get('https://web.whatsapp.com/')
	time.sleep(15)
	#print('Scanning is complete..')

	user_name_list = []
	print()
	print()
	n=int(input("Enter the no. of users you want to send the message to: "))
	for i in range(n):
		user=input("User"+str(i+1)+":")
		user_name_list.append(user)

	scheduled_time = input("Enter the time at which you want to send the message: ")

	for user_name in user_name_list:
		try:
			user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
			user.click()
		except NoSuchElementException as se:
			new_chat(user_name)

		schedule.every().thursday.at(scheduled_time).do(send_message) 

		while True: 
		  
		    # Checks whether a scheduled task  
		    # is pending to run or not 
		    schedule.run_pending() 
		    time.sleep(1) 


		# Typing message into message box
		#message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
		#message_box.send_keys('Hi, I am WhatsApp bot. Lets go bois. ♥'+Keys.ENTER)
		#time.sleep(1)
		#message_box = chrome_browser.find_element_by_xpath('//div[@class="_1JNuk"]')
		#message_box.click()
		#time.sleep(20)

	chrome_browser.close()

