import re 

from robobrowser import RoboBrowser

br = RoboBrowser()
#br.open is a function that takes an argument that's a URL and opens it.
br.open("https://newyork.ucbtrainingcenter.com/login")
#br.get_form tells Python to get the form on the page. Specifics must be added in the event that there are multiple forms on the page.
form = br.get_form()
#These are the fields of the form. The personal details can be stored in a .config file imported above.
form['email'] = 'ron.y.kagan@gmail.com'
form['password'] = 'r12585'
#Submit the form
br.submit_form(form)

#Source code of the target page converted into a parsed string
src = str(br.parsed())

#These variables dictate where the RoboBrowser should start seeking and end seeking website elements
start = '<h1 class="notch_black">Location &amp; Directions'
end = '</h4>'

#This regular expression pulls out the desired info
result = re.search('%s(.*)%s' % (start, end), src).group(1)

#This prints the result
print(result)