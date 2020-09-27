from itertools import permutations


def rSubset(arr, r):

    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(arr, r)))
    return list(permutations(arr, r))


def pandigital(arr):
    if int(str(arr[1])+str(arr[2])+str(arr[3])) % 2 == 0 and int(str(arr[2]) \
        + str(arr[3])+str(arr[4])) % 3 == 0 and int(str(arr[3])+str(arr[4]) \
        + str(arr[5])) % 5 == 0 and int(str(arr[4])+str(arr[5])+str(arr[6])) \
        % 7 == 0 and int(str(arr[5])+str(arr[6])+str(arr[7])) % 11 == 0 and \
        int(str(arr[6])+str(arr[7])+str(arr[8])) % 13 == 0 and \
        int(str(arr[7])+str(arr[8])+str(arr[9])) % 17 == 0:
        return True


def strtofloat(arr):
    return float(''.join(str(x) for x in arr))


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    r = 10
    ans = rSubset(arr, r)
    ans[:] = [x for x in ans if x[0] != 0 and pandigital(x)]
    answer = 0
    for x in range(len(ans)):
        answer += strtofloat(ans[x])
    print(answer)
