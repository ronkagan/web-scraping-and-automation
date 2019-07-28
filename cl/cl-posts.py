from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from pprint import pprint
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import urllib.request

class CraigslistScraper(object):
	def __init__(self):
		self.url = "https://newyork.craigslist.org/brk/fbh/d/dishwasher-part-time/6942991685.html"
		self.driver = webdriver.Chrome()
		self.delay = 5

	def load_craigslist_url(self):
		self.driver.get(self.url)

	def extract_post_information(self):
		try:
			post = self.driver.find_element_by_xpath("//button[@class=\"reply-button js-only\"]").click()
			time.sleep(1)
			email = self.driver.find_element_by_class_name("reply-email-address")
			hiddenemail = email.find_element_by_xpath("//a[@class=\"mailapp\"]").text
			print(hiddenemail)
		except TimeoutException:
			print("Loading took too much time, try raising the delay")

	def quit(self):
		self.driver.close()

scraper = CraigslistScraper()
scraper.load_craigslist_url()
hiddenemail = scraper.extract_post_information()
scraper.quit()