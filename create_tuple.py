n = int(input())
k = int(input())
int_list = list(map(int, input().split()))
tuple_list = []
for i in range(n-k+1):
    temp_list_ori = int_list[i:(i+k)]
    temp_list = temp_list_ori.copy()
    tuple_list.append(tuple(temp_list))
    for j in range(1,k):
        for a in range(k+i, n):
            temp_list[j] = int_list[a]
            tuple_list.append(tuple(temp_list))
            temp_list = temp_list_ori.copy()

print(tuple_list)