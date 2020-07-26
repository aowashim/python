def getSubString(s, n):
    subStrList = []
    for i in range(n):
        for j in range(i, n):
            subStrList.append(s[i: j+1])

    return subStrList


if __name__ == "__main__":
    s = input('str : ')
    res = getSubString(s, len(s))
    print(res, set(res), sep='\n')
