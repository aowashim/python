def calExpo(a, b):
    result = 1
    while b:
        if b % 2 == 1:
            result = (result * a) % 1000000007
        a = (a * a) % 1000000007
        b //= 2
        
    return result

t = int(input())
while t:
    n, a = map(int, input().split())
    sum_ = 0
    c = 1

    if a == 0:
        sum_ = 0
    elif a == 1:
        sum_ = n
    else:
        while n:
            ts = calExpo(a, c)
            sum_ = (sum_ + ts) % 1000000007
            c += 2
            a = (ts * a) % 1000000007
            n -= 1

    print(sum_)
    t -= 1