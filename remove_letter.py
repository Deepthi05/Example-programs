def remove_letter(letter, strng):
	"""
	>>> remove_letter('a', 'apple')
	'pple'
	>>> remove_letter('a', 'banana')
	'bnn'
	>>> remove_letter('z', 'banana')
	'banana'
	>>> remove_letter('i', 'Mississippi')
	'Msssspp'
	"""
	if letter in strng:
		result = strng.replace(letter, "")
		return result
	else:
		return strng


if __name__ == "__main__":
	import doctest
	doctest.testmod()