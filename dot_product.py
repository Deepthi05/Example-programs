def dot_product(u, v):
	"""
	>>> dot_product([1, 1], [1, 1])
	2
	>>> dot_product([1, 2], [1, 4])
	9
	>>> dot_product([1, 2, 1], [1, 4, 3])
	12
	>>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
	0
	"""
	result = []
	count = 0
	for a, i in enumerate(u):
		for b, j in enumerate(v):
			if a==b:
				result.append(i*j)
			j+=1
		i+=1
	for num in result:
		count= count + num
	return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
				
			