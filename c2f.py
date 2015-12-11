def c2f(t):
	"""
	>>> c2f(0)
	32
	>>> c2f(100)
	212
	>>> c2f(-40)
	-40
	>>> c2f(12)
	54
	>>> c2f(18)
	64
	>>> c2f(-48)
	-54
	"""
	return int(round((t*1.8)+32))


if __name__ == "__main__":
    import doctest
    doctest.testmod()