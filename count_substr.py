def count(sub, s):
	"""
	>>> count('is', 'Mississippi')
	2
	>>> count('ban', 'banana')
	1
	>>> count('ana', 'banana')
	2
	>>> count('nana', 'banana')
	1
	>>> count('nanan', 'banana')
	0
	"""
	results = 0
	sub_len = len(sub)
	for i in range(len(s)):
    		if s[i:i+sub_len] == sub:
        		results += 1
	return results
	

if __name__ == "__main__":
	import doctest
	doctest.testmod()
			