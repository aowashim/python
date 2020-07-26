import random

def binarySearch(numList, num, l, r):
    ans = r
    while l <= r:
        mid = (l+r)//2
        
        if numList[mid] <= num:
            l = mid + 1
        else:
            ans = mid
            r = mid - 1
    return ans

#li = [random.randrange(0,550) for i in range(50)]
li = [1,22,3,5,67,4,0,5,3]
li.sort()
n = int(input())
# isFound = binarySearch(li, n, 0, len(li)-1)
# if isFound:
    # print('found')
# else:
    # print('not found')
print(li)
print(binarySearch(li, n, 0, len(li)-1))