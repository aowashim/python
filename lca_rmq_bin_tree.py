from math import log2, ceil
from sys import maxsize


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(arr, segTree, start, end, curNode):
    if start == end:
        segTree[curNode] = arr[start]
        return arr[start]

    mid = (start + end) // 2

    segTree[curNode] = min(buildTree(arr, segTree, start, mid, 2 * curNode + 1),
                           buildTree(arr, segTree, mid + 1, end, 2 * curNode + 2))

    return segTree[curNode]


def query(segTree, start, end, left, right, curNode):
    if left > end or right < start or start > end:
        return maxsize

    if left <= start and right >= end:
        return segTree[curNode]

    mid = (start + end) // 2

    return min(query(segTree, start, mid, left, right, 2 * curNode + 1),
               query(segTree, mid + 1, end, left, right, 2 * curNode + 2))


def makeEulerTour(eulerTour, level, firstOccur, newTree):



def mainFun():
    newTree = Tree()
    n = int(input('Number of vertices : '))
    for _ in range(n):
        u, v = map(int, input().split())
        newTree.addEdge(u, v)

    eulerTour = [0] * (2 * n - 1)
    level = [0] * (2 * n - 1)
    firstOccur = [False] * n

    ht = 2 * (2 ** ceil(log2(n)) - 1)
    segTree = [maxsize] * ht

    buildTree(arr, segTree, 0, n-1, 0)
    for _ in range(5):
        u, v = map(int, input().split())
        print(query(segTree, 0, n-1, u, v, 0))


mainFun()
