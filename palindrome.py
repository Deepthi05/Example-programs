def is_palindrome(s):
	"""
	>>> is_palindrome("abba")
	True
	>>> is_palindrome("abab")
	False
	>>> is_palindrome("tenet")	
	True
	>>> is_palindrome("banana")
	False
	>>> is_palindrome("straw warts")
	True
	"""
	if s == s[::-1]:
		return True
	else:
		return False


if __name__ == "__main__":
	import doctest
	doctest.testmod()