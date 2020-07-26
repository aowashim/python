# naive approach to find lca
# details @ https://www.geeksforgeeks.org/sqrt-square-root-decomposition-set-2-lca-tree-osqrth-time/

from collections import defaultdict


class Tree:
    
    def __init__(self, n):
        self.tree = defaultdict(list)
        self.depth = [-1] * (n + 1)
        self.parent = [0] * (n + 1)

    def addEdge(self, u, v):
        self.tree[u].append(v)
        self.tree[v].append(u)

    def dfs(self, cur, prev):

        #print(cur, end=' ')

        self.depth[cur] = self.depth[prev] + 1
        self.parent[cur] = prev

        for i in self.tree[cur]:
            if i != prev:
                self.dfs(i, cur)

    def lca(self, u, v, path):
        
        if u == v:
            path.append(v)
            return path
            #return u

        elif self.depth[u] > self.depth[v]:
            u, v = v, u

        path.append(v)
        v = self.parent[v]
        return self.lca(u, v, path)

def main():
    with open('text_1.txt', 'r') as f:
        v, n = map(int, f.readline().split())
        t = Tree(v)
        for _ in range(n):
            u, v = map(int, f.readline().split())
            t.addEdge(u, v)

    path = []
    t.dfs(1, 0)
    path = t.lca(8, 11, path)
    print(path)
    #print(t.depth, t.parent, sep='\n')


main()