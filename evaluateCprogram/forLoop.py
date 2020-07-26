from printPresentInt import findVar, isPresent, calInt, printVar


def findComp(str1):
    res = ''

    if isPresent(str1, '<=') != -1:
        res = 'le'
    
    elif isPresent(str1, '<') != -1:
        res = 'l'

    if isPresent(str1, '>=') != -1:
        res = 'ge'

    elif isPresent(str1, '>') != -1:
        res = 'g'

    return res


def findSign(str1):
    sign = ''

    if isPresent(str1, '+') != -1:
        sign = '+'

    elif isPresent(str1, '-') != -1:
        sign = '-'

    elif isPresent(str1, '*') != -1:
        sign = '*'

    else:
        sign = '/'

    return sign


def calNxtLine(nxtLine, varDict):
    eq = isPresent(nxtLine, '=')
    nCur = findVar(nxtLine[: eq], varDict)

    ns = findSign(nxtLine[eq :])
    pos = isPresent(nxtLine, ns)

    tmp = findVar(nxtLine[eq : pos], varDict)
    if tmp == 1:
        nl = calInt(nxtLine[eq + 1: pos])

    else:
        nl = tmp

    tmp = findVar(nxtLine[pos :], varDict)
    if tmp == 1:
        nr = calInt(nxtLine[pos + 1:])

    else:
        nr = tmp

    return (nCur, nl, nr, ns)


def evalExpr(curLine, nl, nr, varDict, nxtLine, ns, i, sign, red, nCur):
    
    val1, val2 = nl, nr

    if type(nl) != int:
        val1 = varDict[nl]

    if type(nr) != int:
        val2 = varDict[nr]
    
    print(f"\n[ {curLine} ] >>>> ", end=' ')
    printVar(varDict)

    if ns == '+':
        varDict[nCur] = val1 + val2

    elif ns == '-':
        varDict[nCur] = val1 - val2

    elif ns == '*':
        varDict[nCur] = val1 * val2

    else:
        varDict[nCur] = val1 // val2

    print(f"\n[ {nxtLine} ] >>>> ", end=' ')
    printVar(varDict)

    if sign == '+':
        i += red

    elif sign == '-':
        i -= red

    elif sign == '*':
        i *= red

    else:
        i //= red

    return i


def printLoop(varDict, curVar, j, red, curLine, nxtLine, cmp, sign):
    #print(varDict, curVar, j, red, curLine, nxtLine, cmp, sign)
    nCur, nl, nr, ns = calNxtLine(nxtLine, varDict)
                    
    i = varDict[curVar]
    if cmp == 'l':
        while i < j:
            i = evalExpr(curLine, nl, nr, varDict, nxtLine, ns, i, sign, red, nCur)
            varDict[curVar] = i

    elif cmp == 'le':
        while i <= j:
            i = evalExpr(curLine, nl, nr, varDict, nxtLine, ns, i, sign, red, nCur)
            varDict[curVar] = i

    elif cmp == 'g':
        while i > j:
            i = evalExpr(curLine, nl, nr, varDict, nxtLine, ns, i, sign, red, nCur)
            varDict[curVar] = i

    else:
        while i >= j:
            i = evalExpr(curLine, nl, nr, varDict, nxtLine, ns, i, sign, red, nCur)
            varDict[curVar] = i


def calForLoop(varDict, curLine, nxtLine):
    parts = curLine.split(';')
    #print(parts)
    curVar = findVar(parts[0], varDict)
    eq = isPresent(parts[0], '=')
    val = findVar(parts[0][eq + 1 :], varDict)
    
    if val == 1:
        varDict[curVar] = calInt(parts[0][eq + 1 :])

    else:
        varDict[curVar] = varDict[val]

    cmp = findComp(parts[1])
    pos = isPresent(parts[1], cmp)
    
    tmp = findVar(parts[1][pos + 1 :], varDict)

    if tmp == 1:
        j = calInt(parts[1][pos + 1 :])

    else:
        j = varDict[tmp]

    sign = findSign(parts[2])

    signPos = isPresent(parts[2], sign)
    last = isPresent(parts[2], ')')
    red = calInt(parts[2][signPos + 1 : last])

    printLoop(varDict, curVar, j, red, curLine, nxtLine, cmp, sign)
