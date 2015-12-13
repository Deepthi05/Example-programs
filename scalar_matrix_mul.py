def scalar_mult(n, m):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> scalar_mult(3, a)
      [[3, 6], [9, 12]]
      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
      >>> scalar_mult(10, b)
      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
      >>> b
      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """

    new_matrix = []
    for row in m:
        new_row = []        
        for value in row:
            new_row += [value*n]
        new_matrix += [new_row]
    return new_matrix    

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()