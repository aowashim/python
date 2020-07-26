from collections import defaultdict
from math import ceil, log2


class Tree:
    def __init__(self, n, ht):
        self.tree = defaultdict(list)
        self.size = n
        self.height = ht
        self.depth = [-1] * n
        self.parent = [[-1 for _ in range(ht + 1)] for _ in range(n)]

    def addEdge(self, u, v):
        self.tree[u].append(v)
        self.tree[v].append(u)


def dfs(ct, s, e):
    vis = [False] * ct.size
    stack = []
    stack.append(s)
    vis[s] = True
    ct.depth[s] = 0
    ct.parent[s][0] = 0

    while stack:
        s = stack.pop()
        for i in ct.tree[s]:
            if not vis[i]:
                vis[i] = True
                stack.append(i)
                ct.depth[i] = ct.depth[s] + 1
                ct.parent[i][0] = s


def sparseTable(ct):
    for i in range(1, ct.height + 1):
        for node in range(1, ct.size):
            if ct.parent[node][i - 1] != -1:
                ct.parent[node][i] = ct.parent[ct.parent[node][i - 1]][i - 1]


def lca(ct, u, v):
    if ct.depth[v] < ct.depth[u]:
        u, v = v, u

    diff = ct.depth[v] - ct.depth[u]

    for i in range(ct.height + 1):
        if (diff >> i) & 1:
            v = ct.parent[v][i]

        if diff == 0:
            break

    if u == v:
        return u
    
    for i in range(ct.height, -1, -1):
        if ct.parent[u][i] != ct.parent[v][i]:
            u = ct.parent[u][i]
            v = ct.parent[v][i]

    return ct.parent[u][0]


def mainFun():
    #v, e = map(int, input('V E : ').split())
    v = 9
    ct = Tree(v + 1, ceil(log2(v)))

    # for _ in range(e):
    #     u, v = map(int, input('u v : ').split())
    #     ct.addEdge(u, v)

    ct.addEdge(1, 2)
    ct.addEdge(2, 3)
    ct.addEdge(3, 4)
    ct.addEdge(4, 5)
    ct.addEdge(5, 6)
    ct.addEdge(6, 7)
    ct.addEdge(7, 8)
    ct.addEdge(8, 9)

    dfs(ct, 1, v)
    sparseTable(ct)

    for _ in range(5):
        u, v = map(int, input('u v : ').split())
        print(lca(ct, u, v))


mainFun()