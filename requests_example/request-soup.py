import requests
from bs4 import BeautifulSoup

#https://newyork.craigslist.org/search/mnh/fbh?query=-uber+-pared+-doordash+-postmates&postedToday=1&bundleDuplicates=1
#https://ny.eater.com/

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src,'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
	a_tag = h2_tag.find('a')
	urls.append(a_tag.attrs['href'])

print(urls)