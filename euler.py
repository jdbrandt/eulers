"""
Euler problems
Works by Jack Brandt
2015-
"""


def p1():
    """
    Returns int sum of multiples of 3 or 5
    less than 1000.
    Should be 233168
    """
    c = 0
    for i in range(1000):
        if i%3==0 or i%5==0:
            c+=i
    return c

def p2():
    """
    Returns int sum of even Fibonacci #'s
    that are even.
    Should be 4613732
    """
    from operator import add
    fibs = [1,2]
    evens = [2]
    while True:
        if fibs[-1]>4e6:
            del fibs[-1]
            return reduce(add,evens)
        else:
            fibs.append(fibs[-1]+fibs[-2])
            if fibs[-1]%2==0:
                evens.append(fibs[-1])
            
    
            


def p25():
    """
    Returns int index of smallest Fibonacci
    # whose length == 1000, when f_0 = 1 and
    f_1 = 1.
    Should be 4782
    """
    from math import log
    fibs = [1,1]
    while True:
        if len(str(fibs[-1]))==1000:
            return len(fibs)
        else:
            fibs.append(fibs[-1]+fibs[-2])
