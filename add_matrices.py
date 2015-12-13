from itertools import izip
def add_matrices(m1, m2):
	"""
	>>> a = [[1, 2], [3, 4]]
	>>> b = [[2, 2], [2, 2]]
	>>> add_matrices(a, b)
	[[3, 4], [5, 6]]
	>>> c = [[8, 2], [3, 4], [5, 7]]
	>>> d = [[3, 2], [9, 2], [10, 12]]
	>>> add_matrices(c, d)
	[[11, 4], [12, 6], [15, 19]]
	>>> c
	[[8, 2], [3, 4], [5, 7]]
	>>> d
	[[3, 2], [9, 2], [10, 12]]
	"""
	
	
	return [[a+b for a, b in izip(m1, m2)] for m1, m2 in izip(m1, m2)]


if __name__ == '__main__':
    import doctest
    doctest.testmod()