def root2(a, b, h):
    if h == 0:
        return 1, 1
    else:
        return 2 * b + a, b + a


def compute(h):
    count = 0
    y = root2(1, 2, 0)
    for i in range(0, h + 1):
        y = root2(y[0], y[1], i)
        if len(str(y[0])) > len(str(y[1])):
            count = count + 1
    return count


if __name__ == "__main__":
    print(compute(1000))
