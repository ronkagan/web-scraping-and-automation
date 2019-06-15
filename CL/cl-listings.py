from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class CraiglistScraper(object):
	def __init__(self, location, postal, max_price, radius):
		self.location = location
		self.postal = postal
		self.max_price = max_price
		self.radius = radius

		self.url = f"https://{location}.craigslist.org/search/sss?search_distance={radius}&postal={postal}&max_price={max_price}"

	def test(self):
		print(self.url)

location = "sfbay"
postal = "94201"
max_price = "500"
radius = "5"

scraper = CraiglistScraper(location, postal, max_price, radius)

scraper.test()