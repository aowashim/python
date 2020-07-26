def sub_print(s, n, idx, cur):
    if n == idx:
        return
    
    if len(cur) >= 1:
        print(cur)

    for i in range(idx+1, n):
        cur += s[i]
        sub_print(s, n, i, cur)

        cur = cur[:-1]

str1 = input("Enter your string : ")
sub_print(str1, len(str1), -1, "")