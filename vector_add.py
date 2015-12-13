def add_vectors(u, v):
	"""
	>>> add_vectors([1, 0], [1, 1])
	[2, 1]
	>>> add_vectors([1, 2], [1, 4])
	[2, 6]
	>>> add_vectors([1, 2, 1], [1, 4, 3])
	[2, 6, 4]
	>>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
	[13, -4, 13, 5]
	"""
	result = []
	for a, i in enumerate(u):
		for b, j in enumerate(v):
			if a==b:
				result.append(i+j)
			j+=1
		i+=1
	return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()