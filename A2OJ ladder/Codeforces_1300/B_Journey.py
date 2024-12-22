import math

t = int(input())
for _ in range(t):
    n,a,b,c = [int(x) for x in input().split(" ")]

    three = a+b+c 
    two = a+b
    one = a
    days = 0

    if n > three:
        days += (math.floor(n/three))*3
        n = n % three
    if n > two and n <= three:
        days += 3
        n = 0
    if n > two:
        days += (math.floor(n/two))*2
        n = n % two
    if n > one and n <= two:
        days += 2
        n = 0
    if n > one:
        days += (math.floor(n/one))*1
        n = n % one
    if n > 0:
        days += 1
        n = 0

    print(days)



