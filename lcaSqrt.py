# details @ https://www.geeksforgeeks.org/sqrt-square-root-decomposition-set-2-lca-tree-osqrth-time/

from collections import defaultdict

class Tree:
    
    def __init__(self, n):
        self.tree = defaultdict(list)
        self.depth = [0] * (n + 1)
        self.parent = [0] * (n + 1)
        self.jumpParent = [0] * (n + 1)

    def addEdge(self, u, v):
        self.tree[u].append(v)
        self.tree[v].append(u)
 
    def findDP(self, n):
        vis = [False] * n
        stack = [1]
        vis[1] = True

        while(stack):
            cur = stack.pop()
            for i in self.tree[cur]:
                if not vis[i]:
                    vis[i] = True
                    stack.append(i)
                    self.parent[i] = cur
                    self.depth[i] = self.depth[cur] + 1

    def findJP(self, n, bLen):

        vis = [False] * n
        stack = [1]
        vis[1] = True

        while(stack):
            cur = stack.pop()
            for i in self.tree[cur]:
                if not vis[i]:
                    vis[i] = True
                    stack.append(i)
                    if self.depth[i] % bLen == 0:
                        self.jumpParent[i] = cur

                    else:
                        self.jumpParent[i] = self.jumpParent[cur]

    def lca(self, u, v):
        while u != v:
            if self.depth[u] > self.depth[v]:
                u, v = v, u

            v = self.parent[v]

        if u == v:
            return u

    def sqLCA(self, u, v):
        while(self.jumpParent[u] != self.jumpParent[v]):
            if self.depth[u] > self.depth[v]:
                u, v = v, u

            v = self.jumpParent[v]

        return self.lca(u, v)

def main():
    f =  open('input.txt', 'r')
    v, n = map(int, f.readline().split())
    curTree = Tree(v)
    for _ in range(n):
        u, v = map(int, f.readline().split())
        curTree.addEdge(u, v)
    f.close()

    #print(v, n)
    curTree.findDP(12)
    height = max(curTree.depth) + 1
    bLen = int(height ** 0.5) + 1

    curTree.findJP(12, bLen)
    u, v = map(int, input().split())
    lca = curTree.sqLCA(u, v)
    #print(curTree.tree)
    print(lca)
    print(1 + curTree.depth[u] + curTree.depth[v] - 2 * curTree.depth[lca])

main()