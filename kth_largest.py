def partition(arr,low,high,x): 
    for i in range(low, high):
        if arr[i] == x:
            arr[i],arr[high] = arr[high],arr[i]
            break
    i = ( low-1 )
    pivot = arr[high]
  
    for j in range(low , high): 
  
        if   arr[j] < pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    #print(i+1,arr)
    return ( i+1 )

def kLargest(arr, l, r, k):
    n = r-l+1
    if n <= 5:
        #print(arr)
        arr.sort()
        #print(arr[n-k])
        return arr[n-k]
    else:
        mList = []
        for i in range(l, n-1, 5):
            tsa = arr[i : i+5]
            tsa.sort()
            mList.append(tsa[len(tsa) // 2])

        #print(i,n)
        if n-i != 5:
            i -= 5
            tsa = arr[i : n]
            tsa.sort()
            mList.append(tsa[len(tsa) // 2])

        ml = len(mList)
        mom = kLargest(mList, 0, ml-1, ml//2)
        #print(mList)
        #print('mom', mom)
        
        pos = partition(arr, l, r, mom)
         
        if r-pos == k-1:
            return arr[pos]
        elif r-pos < k - 1:
            return kLargest(arr[l:pos], l, pos-1, k-r+pos-1)
        else:
            return kLargest(arr[pos+1:r+1], pos+1, r, k)

li = [1, 2, 4, 5, 6, 7, 8, 0, 11, 13, 12, 36, 26, 17, 19, 41]
#li = [11, 22, 14, 10, 13]
n = int(input())
print(kLargest(li, 0, len(li)-1, n))