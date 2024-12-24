t = int(input())

for _ in range(t):
    n = int(input())

    #x > 3 into 2 coins with value x/4 

    i = 4

    coins = 1

    if n <= 3:
        coins = 1
    else:
        while i <= n:
            i = i*4
            coins = coins*2

    print(coins)
