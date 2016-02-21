""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
	try: 
		fp = open(file_name, 'r')	#opens the file if it exists
		if reset == False:	#does not reset counter
			l = load(fp)					
			counter = l + 1
			fp.close()
			f_new = open(file_name, 'w')	#overwrites file 
			dump(counter, f_new)	#updated count stored in new file
			f_new.close()
			
		else:
			counter = 1	#sets count back to 1
			f_new = open(file_name, 'w')	#overwrites file
			dump(counter, fp)	#stores new count in file
			f_new.close()
		fp.close()
		return counter
	except:
		fp = open(file_name, 'w')	#creates a new file
		counter = 1	#sets a count
		dump(counter, fp)	#stores count in file
		fp.close()
		return counter

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))