def merge(arr, l, r):
    n1 = len(l)
    n2 = len(r)
    
    i , j, k = 0, 0, 0
    while (i < n1 and j < n2):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while(i < n1):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1

def mergeSort(arr):
    lenArr = len(arr)
    if lenArr > 1:
        m = lenArr // 2
        l = arr[:m]
        r = arr[m:]
        mergeSort(l)
        mergeSort(r)
        merge(arr, l, r)

inList = list(map(int, input().split()))
print(inList)
mergeSort(inList)
print(inList)