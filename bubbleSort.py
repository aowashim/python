# bubble sort function
def bubbleSort(arr, size):
    for i in range(size - 1):
        flag = 1
        for j in range(size - 1 - i):
            # swap the values if arr[j] > arr[j + 1]
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 0

        if flag:
            break

def main():
    arr = [1, 33, 0, -1, 2, 3, 2, 9, 7]
    n = len(arr)
    print('Array before print :', *arr)

    bubbleSort(arr, n)

    print('Array after print :', *arr)

main()