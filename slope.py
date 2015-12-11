def slope(x1, y1, x2, y2):
	return float(float(y2-y1)/float(x2-x1))


def intercept(x1, y1, x2, y2):
        """
        >>> intercept(1, 6, 3, 12)
        3.0
        >>> intercept(6, 1, 1, 6)
        7.0
        >>> intercept(4, 6, 12, 8)
        5.0
        """
        a= float (y1+y2)/2
        b= slope(x1,y1,x2,y2)
        c= float (x1+x2)/2
        d= float(a-((c)*(b)))
        return d
        


if __name__ == '__main__':
	import doctest
	doctest.testmod()
