t= int(input())

for _ in range(t):
    n = int(input())
    odds = 0
    evens = 0
    for num in input().split(" "):
        if int(num) % 2 == 0:
            evens += 1
        else:
            odds += 1

    if evens == odds:
        print("Yes")
    else:
        print("No")
