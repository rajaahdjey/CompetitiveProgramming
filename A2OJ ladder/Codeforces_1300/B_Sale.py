n , m = [int(x) for x in input().split(" ")]

tv_prices = [int(x) for x in input().split(" ")]

tv_prices.sort()

max_amt = 0

for price in tv_prices[0:m]:
    if price < 0:
        max_amt -= price

print(max_amt)