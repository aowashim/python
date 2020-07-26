def merge(arr, l, r):
    n1 = len(l)
    n2 = len(r)
    m = min(n1,n2)
    i , j, k = 0, 0, 0
    while (i < m and j < m):
        if l[i] <= r[j]:
            arr.append(l[i])
            i += 1
        else:
            arr.append(r[j])
            j += 1
        k += 1

    while(i < n1):
        arr.append(l[i])
        i += 1
        k += 1

    while j < n2:
        arr.append(r[j])
        j += 1
        k += 1

l = [1,2,3,4]
r = [5,6,7,9]
arr = []
merge(arr, l, r)
print(l, r, sep = "\n")
print(arr)