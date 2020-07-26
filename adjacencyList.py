class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, n):
        self.vertexNum = n
        self.adjList = [None] * self.vertexNum

    def addEdge(self):
        edgeNum = int(input('Enter no. of edges : '))
        for _ in range(edgeNum):
            x, y = map(int, input('Enter edge as x,y : ').split(','))
            newNode = Node(y)
            newNode.next = self.adjList[x]
            self.adjList[x] = newNode

            newNode = Node(x)
            newNode.next = self.adjList[y]
            self.adjList[y] = newNode

    def printList(self):
        print('\nThe adjacency list is : \n')
        for i in range(self.vertexNum):
            print(f'Adjacency list of vertex {i} : ', end='')
            temp = self.adjList[i]
            while temp:
                print(temp.vertex, end=' -> ')
                temp = temp.next
            print()

num = int(input('Enter no. of vertices : '))
graph1 = Graph(num)
graph1.addEdge()
graph1.printList()
