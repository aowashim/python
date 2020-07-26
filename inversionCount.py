def merge(arr, l, r):
    n1 = len(l)
    n2 = len(r)
    invrCnt = 0
    i , j, k = 0, 0, 0
    while (i < n1 and j < n2):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
            invrCnt += n1 - i
        k += 1

    while(i < n1):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1

    return invrCnt

def mergeSort(arr):
    invrCnt = 0
    lenArr = len(arr)
    if lenArr > 1:
        m = lenArr // 2
        l = arr[:m]
        r = arr[m:]
        invrCnt += mergeSort(l)
        invrCnt += mergeSort(r)
        invrCnt += merge(arr, l, r)

    return invrCnt

inList = list(map(int, input().split()))
print(inList)
res = mergeSort(inList)
print(inList)
print(f"Number of inversions = {res}")