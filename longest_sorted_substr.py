s = 'azcbobobegghakl'
mystr = {}
for index in range(len(s)):
  for ind2 in range(index+1,len(s)):
     if s[index:ind2] == ''.join(sorted(s[index:ind2])):
         mystr[s[index:ind2]] = len(s[index:ind2])
     else:
         break

def get_count(mydict_tuple):
    return mydict_tuple[1]

def print_top():
    print sorted(mystr.items(), key=get_count, reverse=True)[0]

print mystr
print_top()