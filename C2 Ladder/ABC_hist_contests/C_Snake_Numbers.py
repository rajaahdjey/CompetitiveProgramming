import math


def count_nums(a):
    digits = []
    while a > 0:
        digits.append(a % 10)
        a = a//10
    digits.reverse()

    n = len(digits)

    res = 0

    for i in range(1,len(digits)+1):
        if i == n:
            res += 1
            break
        print(int(math.pow(digits[0],n-i-1)))
        print(min (digits[i],digits[0]))
        res += int(math.pow(digits[0],n-i-1)) * min (digits[i],digits[0])
        if digits[i] >= digits[0]:
            break
    
    for i in range(0,n):
        max_v = 9
        if i == 0:
            max_v = digits[0]-1
        for j in range(1,max_v+1):
            print(i,j)
            print(int(math.pow(j,n-i-1)))
            res += int(math.pow(j,n-i-1))
    
    return res

a,b = map(int,input().split())

print(count_nums(b) - count_nums(a-1))