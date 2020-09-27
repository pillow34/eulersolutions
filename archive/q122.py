def isbouncy(n):
    flag = False
    test_list = [digit for digit in str(n)]
    test_list1 = test_list[:]
    test_list1.sort()
    if (test_list1 == test_list):
        flag = True
    test_list1.sort(reverse=True)
    if (test_list1 == test_list):
        flag = True
    return flag


def compute():
    upp = 2
    ans = 1
    while (upp-ans) * 1.0 <= 0.99 * upp:
        if isbouncy(upp):
            ans += 1
        upp += 1
    return(upp-1)


if __name__ == "__main__":
    print(compute())
