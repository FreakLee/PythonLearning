
def add(a, b):
    """
    This function adds two numbers.

    >>> add(2, 3)
    5
    >> add(-1, 1)
    0
    """
    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()