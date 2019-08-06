from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import urllib.request
import time

chrome_path = r"/Users/ron/web-scraping-and-automation/chromedriver"
driver = webdriver.Chrome(chrome_path)

class CraiglistScraper(object):
    def __init__(self):
        self.url = """https://newyork.craigslist.org/search/mnh/fbh?query=cook+-fairfield+-staten+-"long+island"+-elmsford+-hackensack+-gig+-uber+-postmates+-handyman+-hora"""

        self.driver = webdriver.Chrome()
        self.delay = 5

    def load_craigslist_url(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result-row")))
            #print("Page is ready")
        except TimeoutException:
            print("Loading took too much time, try raising the delay")

    def extract_post_urls(self):
        url_list = []
        email_list = []
        html_page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html_page, "lxml")
        for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
                print(link["href"])
                url_list.append(link["href"])
                for listitem in url_list:
                        try:
                            self.driver.get(listitem)
                            print(listitem)
                            time.sleep(1)
                            self.driver.find_element_by_xpath("//button[@class=\"reply-button js-only\"]").click()
                            time.sleep(1)
                            email = self.driver.find_element_by_class_name("reply-email-address")
                            hiddenemail = email.find_element_by_xpath("//a[@class=\"mailapp\"]").text
                            print(hiddenemail)
                            email_list.append(hiddenemail)
                        except NoSuchElementException:
                            pass

    def quit(self):
        self.driver.close()

scraper = CraiglistScraper()
scraper.load_craigslist_url()
scraper.extract_post_urls()
scraper.quit()