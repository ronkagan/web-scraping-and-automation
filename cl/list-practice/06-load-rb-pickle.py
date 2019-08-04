# load additional module
import pickle

with open('listfile.data', 'rb') as filehandle:
	# read the data as binary data stream
	urlsList = pickle.load(filehandle)

# pickle works with all kind of Python objects such as strings, numbers, self-defined structures, and every other built-in data structure Python provides.