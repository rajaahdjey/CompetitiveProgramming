t = int(input())

for _ in range(t):
    n = int(input())
    weights = [int(x) for x in input().split()]
    ones = 0
    twos = 0
    for candy in weights:
        if candy == 1:
            ones += 1
        else:
            twos += 1
    
    if (ones == 0):
        if (twos % 2 ==0):
            print("YES")
        else:
            print("NO")
    elif (twos == 0):
        if (ones % 2 ==0):
            print("YES")
        else:
            print("NO")
    elif (ones % 2 == 0) and (twos*2-ones)%2 ==0:
        print("YES")
    else:
        print("NO")

        
