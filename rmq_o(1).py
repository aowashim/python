from math import log2


def preprocess(lookup, n, size, arr):
    for i in range(n):
        lookup[i][0] = i

    for j in range(1, size + 1):
        i = 0
        tPj = 2 ** j
        while i + tPj - 1 < n:
            tmp = i + tPj // 2
            if arr[lookup[i][j - 1]] < arr[lookup[tmp][j - 1]]:
                lookup[i][j] = lookup[i][j - 1]

            else:
                lookup[i][j] = lookup[tmp][j - 1]

            i += 1


def query(arr, lookup, l, r):
    j = int(log2(r - l + 1))
    tPj = 2 ** j

    if arr[lookup[l][j]] < arr[lookup[r - tPj + 1][j]]:
        return arr[lookup[l][j]]

    else:
        return arr[lookup[r - tPj + 1][j]]


def mainFun():
    arr = list(map(int, input('Array : ').split()))
    n = len(arr)

    size = int(log2(n))
    lookup = [[n for _ in range(size + 1)] for _ in range(n)]

    preprocess(lookup, n, size, arr)

    for _ in range(5):
        l, r = map(int, input('l, r : ').split())
        print(query(arr, lookup, l, r))


mainFun()
