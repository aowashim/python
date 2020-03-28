# Roll number : CSB18062

from collections import Counter

def checkString(s):
    lang = ['a', 'b', 'c']
    flag1, flag2, flag3, flag4 = 0, 0, 0, 0
    lenS = len(s)
    if lenS >= 2:
        flag1 = 1

    if flag1:
        if len(set(s)) <= 3:
            flag2 = 1

    if flag1 and flag2:
        d = Counter(s)
        flag3 = 1
        for k in d.keys():
            if k not in lang:
                flag3 = 0
                break

    if flag3:
        if d['c'] == 2:
            if(s[s.find('c') + 1]) == 'c':
                flag4 = 1

    if flag4:
        return True

    return False

with open('user input.txt', 'r') as f:
    print('The strings that belongs to the regular language R :')
    for line in f:
        li = list(line.rstrip('\n').split())
        for wrd in li:
            if checkString(wrd):
                print(wrd)