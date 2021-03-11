import eulerfuncs as ef
import itertools as it
import math as m

ansr = []
ansl = []

def leftTrunc(n):
    if str(n)[1:] == '':
        return ansr
    else:
        if ef.isPrime(n):
            if ef.isPrime(int(str(n)[1:])):
                ansr.append(True)
                return leftTrunc(int(str(n)[1:]))
            else:
                ansr.append(False)
                return [0]
        else:
            return [0]

def rightTrunc(n):
    if str(n)[1:] == '':
        return ansl
    else:
        if ef.isPrime(n):
            if ef.isPrime(int(str(n)[:-1])):
                ansl.append(True)
                return rightTrunc(int(str(n)[:-1]))
            else:
                ansl.append(False)
                return [0]
        else:
            return [0]


act = []

for i in it.count(11,1):
    ansl = []
    ansr = []
    if m.prod(rightTrunc(i)) * m.prod(leftTrunc(i)) == 1:
        act.append(i)
    if len(act) == 11:
        break

# print(act)
print(sum(act))
