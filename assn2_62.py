def check_par(str_par):
    list_par = []
    str_len = len(str_par)
    flag = 0
    
    for i in range(str_len):
        if str_par[i] == '(' or str_par[i] == '{':
            list_par.append(str_par[i])
            
        if len(list_par) == 0:
            flag = 1
            break
            
        elif str_par[i] == ')':
            if list_par[-1] == '(':
                list_par.pop()
            else:
                flag = 1
                break    
            
        elif str_par[i] == '}':
            if list_par[-1] == '{':
                list_par.pop()
            else:
                flag = 1
                break
            
    if flag or len(list_par) != 0:
        return False
        
    else:
        return True
        
def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

def count_par(b):
    count1, count2, count3, count4 = 0, 0, 0, 0
    if True:
        for i in b:
            if i == '(':
                count1 += 1
            elif i == ')':
                count2 += 1
            elif i == '{':
                count3 += 1
            elif i == '}':
                count4 += 1
        if count1 != count2:
            if count1 < count2:
                for j in range(count2-count1):
                    b.remove(')')
            else:
                for j in range(count1-count2):
                    b.remove('(')
        if count3 != count4:
            if count3 < count4:
                for j in range(count4-count3):
                    b.remove('}')
            else:
                for j in range(count3-count4):
                    b.remove('{')
    return b

def print_all_comb(str1):
    if check_par(str1):
        print('Valid.')
    else:
        print('Invalid.')
        b = list(str1)
        a = count_par(b)
        s = ''.join(a)
        #print(s)
        list_all_comb = set(permute_string(s))
        print('The valid combinations are : ')
        for i in list_all_comb:
            if check_par(i):
                print(i)

string = input('Enter your string : ')  
print_all_comb(string)