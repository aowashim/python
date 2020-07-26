from collections import defaultdict
import sys

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        #self.graph[v].append(u)

    def bfs(self, s, d):
        numVertex = len(self.graph)
        visited = [False] * numVertex
        parent = [-1] * numVertex
        dist = [sys.maxsize] * numVertex

        visited[s] = True
        dist[s] = 0
        queue = []
        queue.append(s)

        while queue:
            u = queue.pop(0)
            #print(u, end=' -> ')
            for v in self.graph[u]:
                if not visited[v]:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
                    visited[v] = True

                    if v == d:
                        print(f'The length of shortest path between {s}, {d} is : {dist[d]}.')
                        path = []
                        path.append(d)
                        p = parent[d]
                        while p != -1:
                            path.append(p)
                            p = parent[p]

                        print('And the path is : ', end='')
                        for i in range(len(path)-1, -1, -1):
                            print(path[i], end=' -> ')
                        
                        return True
        return 'Path does not exist.'

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 4) 
g.bfs(1,2)