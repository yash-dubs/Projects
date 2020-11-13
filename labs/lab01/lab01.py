def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    a=[]
    if k>0:
        while len(a) < k:
            a.append(n)
            n=n-1
        list_sum = 1
        for x in a:
            list_sum=list_sum * x
        return list_sum
    else:
        return 1



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    x=[]
    y=str(y)
    x.extend(y)
    list_sum=0
    z=0
    while z < len(x):
        x[z]=int(x[z])
        list_sum=list_sum + x[z]
        z=z+1
    return list_sum



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """

    x=[]
    n=str(n)
    x.extend(n)
    z=0
    if len(x) <= 1:
        return False
    else:
        while z < len(x):
            if x[z] == x[z+1]:
                return True
            z=z+1
            if x[z] == x[-1]:
                return False
