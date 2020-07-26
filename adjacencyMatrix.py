class Graph:
    def __init__(self, numVertex):
        self.aMatrix = [ [0]*numVertex for i in range(numVertex) ]
        self.numVertex = numVertex

    def addEdge(self):
        n = int(input('Enter number of edges : '))
        for _ in range(n):
            x, y = map(int, input('Enter vertex as x,y : ').split(','))
            self.aMatrix[x][y] = 1
            self.aMatrix[y][x] = 1

    def printMatrix(self):
        print('\nThe adjacency matrix is : \n')
        for i in range(self.numVertex):
            for j in range(self.numVertex):
                print(self.aMatrix[i][j], end='  ')
            print()

num = int(input('Enter no. of vertices : '))
graph1 = Graph(num)
graph1.addEdge()
graph1.printMatrix()