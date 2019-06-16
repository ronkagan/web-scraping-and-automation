import csv
from selenium import webdriver

MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3

with open('result.csv', 'w') as f:
	f.write("Buyers, Price \n")

# Open up a browser and head to a webpage
driver = webdriver.Chrome()

for i in range(1, MAX_PAGE_NUM + 1):
	page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
	url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"

	driver.get(url)

	buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
	prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

	num_page_items = len(buyers)
	with open('result.csv', 'a') as f:
		for i in range(num_page_items):
			f.write(buyers[i].text + "," + prices[i].text + "\n")

driver.close()

#driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# Extract lists of "buyers" and "prices" based on xpath


# Print out all of the buyers and prices on the current page
#num_page_items = len(buyers)
#for i in range(num_page_items):
#	print(buyers[i].text + " : " + prices[i].text)

# Clean up (close browser once task is complete)
#