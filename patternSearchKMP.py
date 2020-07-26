def searchPattern(string, pat):
    n = len(string)
    m = len(pat)
    foundAt = []
    i, j = 0, 0
    posArr = makePosArr(pat)

    while i < n:
        if string[i] == pat[j]:
            i += 1
            j += 1
        if j == m:
            foundAt.append(i - j)
            j = posArr[j - 1]
        elif i < n and string[i] != pat[j]:
            if j != 0:
                j = posArr[j - 1]
            else:
                i += 1
    return foundAt


def makePosArr(pat):
    posArr = [0]
    lp = len(pat)
    cur = 0
    i = 1

    while i < lp:
        if pat[i] == pat[cur]:
            cur += 1
            posArr.append(cur)
            i += 1
        else:
            if cur != 0:
                cur = posArr[cur - 1]
            else:
                posArr.append(cur)
                i += 1
    return posArr

s = input()
p = input()
print(searchPattern(s, p))