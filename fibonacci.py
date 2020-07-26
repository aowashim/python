num = int(input("Enter your nuber : "))
lst = [0, 1]
for i in range(2, num+1):
    n_no = lst[i-1] + lst[i-2]
    if n_no > num:
        break
    lst.append(n_no)
print(f"The fibonacci series upto {num} is : {lst}")
