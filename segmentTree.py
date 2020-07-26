# segment tree to count the number of subarrays
# which are divisible by 4

from math import ceil, log2

def buildTree(tArr, node, arr, start, end):
    if start == end:
        tArr[node] = abs(arr[start]) % 4
        return

    mid = (start+end) // 2
    buildTree(tArr, node*2 +1, arr, start, mid)
    buildTree(tArr, node*2 +2, arr, mid+1, end)
    tArr[node] = abs((tArr[node*2 +1] * tArr[node*2 +2])) % 4

def query(tArr, node, start, end, l, r):
    if start > end or l > end or r < start:
        return 1
    
    if l <= start and r >= end:
        return tArr[node] % 4

    mid = (start + end) // 2
    q1 = query(tArr, node*2 +1, start, mid, l, r)
    q2 = query(tArr, node*2 +2, mid+1, end, l, r)
    return (q1 * q2) % 4

def countSubArr(tArr, arr, n):
    cntr = 0
    for i in range(n):
        for j in range(i, n):
            res = query(tArr, 0, 0, n-1, i, j)
            if res != 2:
                cntr += 1
    return cntr

t = int(input())
while t:
    n = int(input())
    aList = list(map(int, input().split()))
    h = ceil(log2(n))
    size = 2 * int(2 ** h) - 1
    tArr = [0] * size
    buildTree(tArr, 0, aList, 0, n-1)
    print(countSubArr(tArr, aList, n))

    t -= 1