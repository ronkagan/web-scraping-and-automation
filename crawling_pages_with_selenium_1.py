from selenium import webdriver

# Open up a browser and head to a webpage
driver = webdriver.Chromium()
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# Extract lists of "buyers" and "prices" based on xpath
buyers = driver.find_elements_by_xpath()