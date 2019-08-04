# read the contents of the output file back into memory
import json

# open output file for reading
with open('listfile-2.txt', 'r') as filehandle:
	basicList = json.load(filehandle)