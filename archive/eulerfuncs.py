import numpy as np
from itertools import product
import math
from functools import reduce
from collections import Counter


def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


def findGCF(n=[1]):
    a = []
    for i in range(int(min(n))+1):
        a.append(i) if max(np.array(n) % i) == 0 else 1
    return max(a)


def findLCM(arr):
    n = len(arr)
    # Find the maximum value in arr[]
    max_num = 0
    for i in range(n):
        if (max_num < arr[i]):
            max_num = arr[i]

    # Initialize result
    res = 1

    # Find all factors that are present
    # in two or more array elements.
    x = 2  # Current factor.
    while (x <= max_num):

        # To store indexes of all array
        # elements that are divisible by x.
        indexes = []
        for j in range(n):
            if (arr[j] % x == 0):
                indexes.append(j)

        # If there are 2 or more array
        # elements that are divisible by x.
        if (len(indexes) >= 2):

            # Reduce all array elements
            # divisible by x.
            for j in range(len(indexes)):
                arr[indexes[j]] = int(arr[indexes[j]] / x)

            res = res * x
        else:
            x += 1

    # Then multiply all reduced
    # array elements
    for i in range(n):
        res = res * arr[i]

    return res


MUL = int.__mul__


def prime_factors(n):
    'Map prime factors to their multiplicity for n'
    d = _divs(n)
    d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)


def _divs(n):
    'Memoized recursive function returning prime factors of n as a list'
    for i in range(2, int(math.sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]


def proper_divs(n):
    '''Return the set of proper divisors of n.'''
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(n)
    except KeyError:
        pass
    return divs or ({1} if n != 1 else set())
