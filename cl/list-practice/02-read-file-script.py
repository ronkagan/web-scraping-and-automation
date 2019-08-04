# define an empty list
urls = []

# open fie and read the content in a list
with open('url_list_file.txt', 'r') as filehandle:
	for line in filehandle:
		# remove linebreak which is the last character of the string
		currentUrl = line[:-1]

		#add item to the list
		urls.append(currentUrl)