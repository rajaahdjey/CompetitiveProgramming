t = int(input())

for _ in range(t):
    k = int(input())
    i = 1
    ele = 1
    while i <= k:
        # print(i,k)
        if i%10 != 3 and i%3 !=0:
            ele = i
            i += 1
        else:
            i+=1
            k+=1
    print(ele)


