from math import ceil, log2
import sys


def buildTree(arr, treeArr, node, start, end):
    # if start == end:
    #     treeArr[node] = arr[start]
    #     return arr[start]

    # mid = (start + end) // 2
    # treeArr[node] = min(buildTree(arr, treeArr, 2*node + 1, start, mid),
    #                     buildTree(arr, treeArr, 2*node + 2, mid+1, end))

    # return treeArr[node]
    if start == end:
        treeArr[node] = arr[start]

    else:
        mid = (start + end) // 2
        
        buildTree(arr, treeArr, 2*node + 1, start, mid)
        buildTree(arr, treeArr, 2*node + 2, mid+1, end)

        if treeArr[2*node + 1] < treeArr[2*node + 2]:
            treeArr[node] = treeArr[2*node + 1]

        else:
            treeArr[node] = treeArr[2*node + 2]


def query(treeArr, node, start, end, l, r):
    if start > end or l > end or r < start:
        return sys.maxsize

    if l <= start and r >= end:
        return treeArr[node]

    mid = (start + end) // 2
    return min(query(treeArr, 2*node + 1, start, mid, l, r),
               query(treeArr, 2*node + 2, mid+1, end, l, r))


inArr = list(map(int, input('Enter array : ').split()))
n = len(inArr)
treeHeight = ceil(log2(n))
size = 2 * int(2**treeHeight) - 1
treeArr = [sys.maxsize] * size

buildTree(inArr, treeArr, 0, 0, n-1)
q = int(input('Enter q : '))
for i in range(q):
    l, r = map(int, input('l r: ').split())
    print('min =', query(treeArr, 0, 0, n-1, l, r))