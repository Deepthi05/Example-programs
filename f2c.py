def f2c(t):
	"""
	>>> f2c(212)
	100
	>>> f2c(32)
	0
	>>> f2c(-40)
	-40
	>>> f2c(36)
	2
	>>> f2c(37)
	3
	>>> f2c(38)
	3
	>>> f2c(39)
	4
	"""
	return int(round(float(5*(t-32))/9))

if __name__ == "__main__":
    import doctest
    doctest.testmod()