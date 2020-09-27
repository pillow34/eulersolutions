import math


def compute():
    one = [x for x in range(1, 101)]
    ans = []
    for n in one:
        r = 1
        while r <= n:
            if math.comb(n, r) >= 1000000:
                ans.append(math.comb(n, r))
            r += 1
    return(len(ans))


if __name__ == "__main__":
    print(compute())
