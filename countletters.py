""" a = "Deepthi"
count D=1, e=2, p=1 etc """

a = raw_input("Enter String whose letters are to be counted!!")

def display(i):
	if i == 32: 
		return "SPACE"
	else:
		return chr(i)

counts = 128 * [0]

for letter in a:
	counts[ord(letter)] += 1

print "%-12s%s\n" % ("Character", "Count")
print "=================\n"

for i in range(len(counts)):
	if counts[i]:
		print "%-12s%d\n" % (display(i), counts[i])

