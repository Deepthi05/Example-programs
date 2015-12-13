def only_odds(numbers):
	"""
	>>> only_odds([1, 3, 4, 6, 7, 8])
	[1, 3, 7]
	>>> only_odds([2, 4, 6, 8, 10, 11, 0])
	[11]
	>>> only_odds([1, 3, 5, 7, 9, 11])
	[1, 3, 5, 7, 9, 11]
	>>> only_odds([4, 0, -1, 2, 6, 7, -4])
	[-1, 7]
	>>> nums = [1, 2, 3, 4]
	>>> only_odds(nums)
	[1, 3]
	>>> nums
	[1, 2, 3, 4]
	"""
	result = []
	for i in numbers:
		if i%2 == 0:
			continue
		else:
			result.append(i)
	return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()