import itertools
from eulerfuncs import fib


def pandigital(s):
    if ''.join(sorted(str(s)[:9])) == '123456789':
        if ''.join(sorted(str(s)[-9:])) == '123456789':
            return True
        else:
            return False
    else:
        return False


def compute():
    ans = []
    for i in itertools.count(1):
        x = fib(i)
        ans.append(x)
        if ''.join(sorted(str(x % 10**9))) == '123456789':
            print(len(ans))
            if ''.join(sorted(str(x)[:9])) == '123456789':
                break
    #print('found')
    return len(ans)


if __name__ == "__main__":
    print(compute())
