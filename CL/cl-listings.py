from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class CraigslistScraper(object):
	def __init__(self, location, postal, max_price, radius):
		self.location = 'newyork'
		self.postal = '10030'
		self.max_price = '100'
		self.radius = '1'

		self.url = "https://newyork.craigslist.org/search/sss?search_distance=1&postal=10030&max_price=100"

		self.driver = webdriver.Chrome()
		self.delay = 5

	def load_craigslist_url(self):
		self.driver.get(self.url)
		try:
			wait = WebDriverWait(self.driver, self.delay)
			wait.until(EC.presence_of_element_located((By.ID, "searchform")))
			#print("Page is ready")
		except TimeoutException:
			print("Loading took too much time, try raising the delay")

	def extract_post_information(self):
		all_posts = self.driver.find_elements_by_class_name("result-row")

		dates = []
		titles = []
		prices = []

		for post in all_posts:
			title = post.text.split("$")

			if title[0] == '':
				title = title[1]
			else:
				title = title[0]

			title = title.split("\n")
			price = title[0]
			title = title[-1]

			title = title.split(" ")
			
			month = title[0]
			day = title[1]
			title = ' '.join(title[2:])
			date = month + " " + day
			
			#print("PRICE: " + price)
			#print("TITLE: " + title)
			#print("DATE: " + date)

			titles.append(title)		
			prices.append(price)
			dates.append(date)
		return titles, prices, dates

	def extract_post_urls(self):
		url_list = []
		html_page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html_page, "lxml")
		for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
				print(link["href"])
				url_list.append(link["href"])
		return url_list

	def quit(self):
		self.driver.close()

location = "newyork"
postal = "10030"
max_price = "100"
radius = "1"

scraper = CraiglistScraper(location, postal, max_price, radius)
scraper.load_craigslist_url()
titles, prices, dates = scraper.extract_post_information()
print(titles)
#scraper.extract_post_urls()
scraper.quit()