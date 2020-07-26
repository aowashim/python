# https://www.hackerrank.com/topics/mos-algorithm
# square root decomposition to find sum in a range

def makeBlock(arr, bLen):
    block = [0] * bLen
    
    for i in range(n):
        block[i // bLen] += arr[i]

    return block

def query(l, r, arr, block, bLen):
    sum_ = 0
    cl, cr = l // bLen, r // bLen
    if cl == cr:
        for i in range(l, r+1):
            sum_ += arr[i]
    else:
        for i in range(l, (cl+1) * bLen):
            sum_ += arr[i]

        for i in range(cl+1, cr):
            sum_ += block[i]

        for i in range(cr*bLen, r+1):
            sum_ += arr[i]

    return sum_

arr = list(map(int, input('Array : ').split()))
n = len(arr)
bLen = int(n ** 0.5) + 1

block = makeBlock(arr, bLen)

q = int(input('q : '))
while q:
    l, r = map(int, input('l, r : ').split())
    print('Sum =', query(l, r, arr, block, bLen))

    q -= 1