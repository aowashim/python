from collections import defaultdict
from math import log2
import sys

sys.setrecursionlimit(10**6)
#pos = 0


class Tree:
    def __init__(self):
        self.tree = defaultdict(list)

    def addEdge(self, u, v):
        self.tree[u].append(v)
        self.tree[v].append(u)


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
        return lookup[l][j]

    else:
        return lookup[r - tPj + 1][j]


def dfs(cur, prev, dep, eulerTour, depth, firstOcurr, ct, parent):
    global pos
    if firstOcurr[cur] == -1:
        firstOcurr[cur] = pos

    pos += 1
    eulerTour.append(cur)
    parent[cur] = prev
    depth[cur] = dep

    for node in ct.tree[cur]:
        if node != prev:
            dfs(node, cur, dep + 1, eulerTour, depth, firstOcurr, ct, parent)
            eulerTour.append(cur)
            pos += 1


# def dfs(cur, prev, dep, eulerTour, depth, firstOcurr, ct, parent, n, pos):
#     vis = [False] * n
#     stack = []
#     stack.append(cur)

#     vis[cur] = True
#     depth[cur] = 0
#     parent[cur] = 0
#     eulerTour.append(cur)
#     firstOcurr[cur] = pos
#     pos += 1

#     flag = True

#     while stack:
#         s = stack.pop()
#         if depth[s] == depth[eulerTour[-1]] and s != eulerTour[-1]:
#             eulerTour.append(parent[s])

#         for i in ct.tree[s]:
#             if not vis[i]:
#                 flag = False
#                 vis[i] = True
#                 stack.append(i)
#                 depth[i] = depth[s] + 1
#                 parent[i] = s

#         if flag:
#             eulerTour.append(parent[s])


def findLca(u, v, eulerTour, firstOcurr, lookup, eulerDepth):
    if u == v:
        return u

    if firstOcurr[u] > firstOcurr[v]:
        u, v = v, u

    u = firstOcurr[u]
    v = firstOcurr[v]

    return eulerTour[query(eulerDepth, lookup, u, v)]


def findNodeNum(u, v, lca, depth):
    return (1 + depth[u] + depth[v] - 2 * depth[lca])


def calMinDiff(parent, aList, u, v, lca):
    path = []

    while u != lca:
        path.append(aList[u - 1])
        u = parent[u]

    while v != lca:
        path.append(aList[v - 1])
        v = parent[v]

    path.append(aList[lca - 1])

    dif = 101
    pathLen = len(path)
    path.sort()
    for i in range(pathLen - 1):
        curDif = path[i + 1] - path[i]
        if curDif < dif:
            dif = curDif

    print(dif)


def mainFun():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        aList = list(map(int, input().split()))

        ct = Tree()

        for _ in range(n - 1):
            u, v = map(int, input().split())
            ct.addEdge(u, v)

        eulerTour = []
        depth = [-1] * (n + 1)
        parent = [-1] * (n + 1)
        firstOcurr = [-1] * (n + 1)
        dfs(1, 0, 0, eulerTour, depth, firstOcurr, ct, parent, n + 1)

        eulerDepth = []
        for i in eulerTour:
            eulerDepth.append(depth[i])

        eln = 2 * n - 1
        size = int(log2(eln))
        lookup = [[-1 for _ in range(size + 1)] for _ in range(eln)]

        preprocess(lookup, eln, size, eulerDepth)

        for _ in range(q):
            a, b = map(int, input().split())
            lca = findLca(a, b, eulerTour, firstOcurr, lookup, eulerDepth)

            num = findNodeNum(a, b, lca, depth)
            if num > 100:
                print('0')

            else:
                calMinDiff(parent, aList, a, b, lca)


mainFun()
