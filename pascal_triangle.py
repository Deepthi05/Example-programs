def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    #print line    
    return line
n=7
for i in range(1,n):
    print ''.rjust(n-i),
    for elem in pascal(i):
       print repr(elem),' ',
    print ''