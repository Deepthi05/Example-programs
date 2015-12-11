def sum_of_squares_of_digits(n):
	"""
	>>> sum_of_squares_of_digits(1)
	1
	>>> sum_of_squares_of_digits(9)
	81
	>>> sum_of_squares_of_digits(11)
	2
	>>> sum_of_squares_of_digits(121)
	6
	>>> sum_of_squares_of_digits(987)
	194
	"""
	n = str(n)
	r = 0
	for i in n:
		i = int(i)**2
		r = r+i
	return r

if __name__ == "__main__":
    import doctest
    doctest.testmod()