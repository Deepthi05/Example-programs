def add_row(matrix):
	y = len(matrix[0])

	matrix2 = matrix[:]
        for z in range(1):  		
		matrix2 += [[0] * y]
	return matrix2

def add_column(matrix):
    x = len(matrix)

    matrix2 = [d[:] for d in matrix]
    for z in range(x):
        matrix2[z] += [0]
    return matrix2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
