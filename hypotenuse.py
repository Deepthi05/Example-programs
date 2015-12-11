from math import sqrt

def hypotenuse(m,n):
	"""
	>>> hypotenuse(3,4)
	5.0
	>>> hypotenuse(12,5)
	13.0
	>>> hypotenuse(7,24)
	25.0
	"""
	return sqrt((m**2)+(n**2))


if __name__=='__main__':
	import doctest
	doctest.testmod()
	
