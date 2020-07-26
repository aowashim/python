from printPresentInt import findVar, isPresent, calInt, printVar
from forLoop import calForLoop


def mathOps(curLine, varDict, isEql, pos, op):
    curVar = findVar(curLine[: isEql], varDict)

    vl = findVar(curLine[isEql: pos], varDict)
    if vl == 1:
        vl = calInt(curLine[isEql + 1: pos])
    else:
        vl = varDict[vl]

    vr = findVar(curLine[pos:], varDict)
    if vr == 1:
        vr = calInt(curLine[pos + 1: -1])
    else:
        vr = varDict[vr]

    if op == '+':
        varDict[curVar] = vl + vr

    elif op == '*':
        varDict[curVar] = vl * vr

    elif op == '-':
        varDict[curVar] = vl - vr

    else:
        varDict[curVar] = vl // vr


def assignVar(curLine, varDict, pos):
    curVar = findVar(curLine[: pos], varDict)

    tmp = findVar(curLine[pos + 1:], varDict)

    if tmp != 1:
        varDict[curVar] = varDict[tmp]

    else:
        varDict[curVar] = calInt(curLine[pos + 1: -1])


def calVar(curLine, varDict):
    isPos = isPresent(curLine, '+')
    isNeg = isPresent(curLine, '-')
    isMul = isPresent(curLine, '*')
    isDiv = isPresent(curLine, '/')
    isEql = isPresent(curLine, '=')

    if isPos == isNeg == isMul == isDiv == -1:
        if isEql != -1:
            assignVar(curLine, varDict, isEql)

    elif isEql != -1:
        if isPos != -1:
            mathOps(curLine, varDict, isEql, isPos, '+')

        elif isNeg != -1:
            mathOps(curLine, varDict, isEql, isNeg, '-')

        elif isMul != -1:
            mathOps(curLine, varDict, isEql, isMul, '*')

        elif isDiv != -1:
            mathOps(curLine, varDict, isEql, isDiv, '/')


# the program starts here
def fileRead():
    varDict = {}
    varStr = input('Enter variables separated by space : ').split()
    for s in varStr:
        varDict[s] = 0

    with open('cProgram.txt', 'r') as f:
        curLine = f.readline().strip()
        while isPresent(curLine, 'main()') == -1:
            curLine = f.readline().strip()

        curLine = f.readline().strip()
        while isPresent(curLine, 'int') == -1:
            curLine = f.readline().strip()

        for curLine in f:
            curLine = curLine.strip()
            if curLine.strip() == '' or curLine.strip() == '{':
                continue

            if isPresent(curLine, 'printf') == -1 or isPresent(curLine, 'return') == -1:
                if isPresent(curLine, 'for') != -1:
                    #print('yes')
                    calForLoop(varDict, curLine, f.readline().strip())

                else:
                    calVar(curLine, varDict)

            print(f"\n[ {curLine} ] >>>> ", end=' ')
            printVar(varDict)
            #curLine = f.readline().strip()


fileRead()
