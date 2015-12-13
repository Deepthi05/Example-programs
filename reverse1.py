def reverse(s):
	"""
	>>> reverse("happy")
	'yppah'
	>>> reverse("Python")
	'nohtyP'
	>>> reverse("")
	''
	>>> reverse("P")
	'P'
	"""
	return s[::-1]
		
		
if __name__ == "__main__":
	import doctest
	doctest.testmod()