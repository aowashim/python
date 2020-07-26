# to find the parity of permutation (even or odd)
def findParity(listPer, lenPer):

    newList = listPer.copy()
    totalTrans = 0

    for i in range(1, lenPer):
        while newList[i] != i:
            totalTrans += 1
            j = newList[i]
            newList[i], newList[j] = newList[j], newList[i]

    if totalTrans % 2 == 0:
        return True

    else:
        return False


# to get all the cycles of the permutation
def getCycle(listPer, lenPer):

    listOfCycles = []

    for i in range(1, lenPer):
        cntr = 0
        curCycle = []
        while listPer[i] != i:
            j = listPer[i]
            listPer[i], listPer[j] = listPer[j], listPer[i]
            cntr += 1
            curCycle.append((i, j))

        listOfCycles.append((cntr % 2, cntr, curCycle))

    return listOfCycles


def printOut(listOfCycles):

    print(listOfCycles)
    numOfOps, cycleLen = 0, 0
    for element in listOfCycles:
        if element[0] == 0:
            numOfOps += element[1] // 2

        else:
            numOfOps += (element[1] // 2 + 1)

        cycleLen += 1

    print(numOfOps)

    for i in range(cycleLen):
        if listOfCycles[i][0]:
            for j in range(0, listOfCycles[i][1], 2):
                print(listOfCycles[i][2][j][0], listOfCycles[i]
                      [2][j][1], listOfCycles[i][2][j + 1][1])
        else:
            break

    flag = False
    s = 0
    for k in range(i, cycleLen):
        if flag:
            cur = listOfCycles[k][2][0]
            print(prev[0], prev[1], cur[1])
            print(cur[0], cur[1], prev[1])

        for j in range(s, listOfCycles[k][1], 2):
            if s == 0:
                prev = listOfCycles[k][2][-1]
                flag = True
                s = 2
            
            else:
                s = 0
                flag = False

            print(listOfCycles[k][2][j][0], listOfCycles[k]
                  [2][j][1], listOfCycles[k][2][j + 1][1])


def main():

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        listPer = list(map(int, input().split()))

        listPer.insert(0, 0)

        if findParity(listPer, n + 1):
            listOfCycles = getCycle(listPer, n + 1)
            listOfCycles.sort(key=lambda i: i[0])
            printOut(listOfCycles)

        else:
            print(-1)


main()
