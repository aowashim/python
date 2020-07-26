from time import sleep


def printVar(varDict):
    for k in varDict:
        print(k, '=', varDict[k], end=', ')

    print('\n')
    sleep(0.8)


def isPresent(str1, s):
    lenStr1 = len(str1)
    lenS = len(s)

    i, j, pos = 0, 0, -1

    while i < lenStr1:
        while str1[i] == s[j]:
            i += 1
            j += 1

            if j == lenS:
                pos = i - 1
                return pos

        j = 0
        i += 1

    return pos


def calInt(str1):
    return int(str1.strip())


def findVar(str1, varDict):
    for k in varDict:
        if isPresent(str1, k) != -1:
            return k


    return 1
