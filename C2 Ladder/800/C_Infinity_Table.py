from math import sqrt
t = int(input())

for _ in range(t):
    ans =(1,1)
    k = int(input())
    nearest_square = int(sqrt(k)//1)
    # print(nearest_square)
    num = nearest_square**2 + 1
    # print(num)
    if num > k:
        ans = (int(sqrt(k)//1) , 1)
    else:
        for i in range(0,nearest_square+1):
            if num + i == k:
                ans = (i+1,nearest_square+1)
        for j in range(0,nearest_square+1):
            if num + nearest_square + j == k:
                ans = (nearest_square+1,nearest_square+1-j)
    print(*ans)

