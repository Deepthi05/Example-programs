def add_row(matrix):
	"""
	>>> m = [[0, 0], [0, 0]]
	>>> add_row(m)
	[[0, 0], [0, 0], [0, 0]]
	>>> n = [[3, 2, 5], [1, 4, 7]]
	>>> add_row(n)
	[[3, 2, 5], [1, 4, 7], [0, 0, 0]]
	>>> n
	[[3, 2, 5], [1, 4, 7]]
	"""
	y = len(matrix[0])

	matrix2 = matrix[:]
        for z in range(1):  		
		matrix2 += [[0] * y]
	return matrix2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
