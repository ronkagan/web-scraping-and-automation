# write a list of mixed variable types to an output file using the json module
import json

# define list with values
basicList = [1, "Cape Town", 4.6]

# open output file for writing
with open('listfile-2.txt', 'w') as filehandle:
	json.dump(basicList, filehandle)