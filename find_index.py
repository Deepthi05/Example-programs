strg = raw_input("Enter string: ")
ch = raw_input("Enter character to search and return index: ")

def find(a,b):
	index = 0
	while index < len(a):
		if a[index] == b:
			print "ch is in index %s " %index
		elif a[index] != b:
			print "Ch doesnt exists"
		index += 1
		

find(strg,ch)