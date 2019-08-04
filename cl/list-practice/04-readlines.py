# define empty list
urls_list = []

# open file and read the content in a list
with open('listfile.txt', 'r') as filehandle:
	urls = [current_url.rstrip() for current_url in filehandle.readlines()]
# Having opened the file listfile.txt in line 5, re-establishing the list takes place entirely in line 6.
# In a `for` loop from each line, the linebreak character is removed using the `rstrip()` method.
# The string is added to the list of urls as a new list item.