from collections import defaultdict
from math import log2

pos = 0


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


def dfs(cur, prev, dep, eulerTour, depth, firstOcurr, ct):
    global pos
    if firstOcurr[cur] == -1:
        firstOcurr[cur] = pos

    pos += 1
    eulerTour.append(cur)
    depth[cur] = dep

    for node in ct.tree[cur]:
        if node != prev:
            dfs(node, cur, dep + 1, eulerTour, depth, firstOcurr, ct)
            eulerTour.append(cur)
            pos += 1


def findLca(u, v, eulerTour, firstOcurr, lookup, eulerDepth):
    if u == v:
        return u

    if firstOcurr[u] > firstOcurr[v]:
        u, v = v, u

    u = firstOcurr[u]
    v = firstOcurr[v]

    return eulerTour[query(eulerDepth, lookup, u, v)]


def mainFun():
    ct = Tree()
    n = 6

    ct.addEdge(1, 2)
    ct.addEdge(2, 3)
    ct.addEdge(2, 4)
    ct.addEdge(1, 5)
    ct.addEdge(5, 6)

    eulerTour = []
    depth = [-1] * (n + 1)
    firstOcurr = [-1] * (n + 1)
    dfs(1, 0, 0, eulerTour, depth, firstOcurr, ct)

    eulerDepth = []
    for i in eulerTour:
        eulerDepth.append(depth[i])

    eln = 2 * n - 1
    size = int(log2(eln))
    lookup = [[-1 for _ in range(size + 1)] for _ in range(eln)]

    preprocess(lookup, eln, size, eulerDepth)

    print(eulerTour, eulerDepth, firstOcurr, sep='\n')
    for _ in range(5):
        u, v = map(int, input('u v : ').split())
        print(findLca(u, v, eulerTour, firstOcurr, lookup, eulerDepth))


mainFun()
