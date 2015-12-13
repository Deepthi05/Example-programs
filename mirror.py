def mirror(s):
	"""
	>>> mirror("good")
	'gooddoog'
	>>> mirror("yes")
	'yessey'
	>>> mirror("Python")
	'PythonnohtyP'
	>>> mirror("")
	''
	>>> mirror("a")
	'aa'
	"""
	rev = s[::-1]
	result = s+rev
	return result

if __name__ == "__main__":
	import doctest
	doctest.testmod()