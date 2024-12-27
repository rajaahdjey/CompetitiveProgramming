n , m = [int(x) for x in input().split(" ")]

prices = [int(x) for x in input().split(" ")]

prices.sort()

min_p = 0
max_p = 0
num_people_min = n
num_people_max = n
#4 passengers to fill
# 6 sets ..

for price in prices:
    x = price
    if num_people_min == 0:
        break
    while num_people_min >0 and x > 0:
        min_p += x
        x -= 1
        num_people_min -= 1

i = m - 1

#fill max to min, but keep checking if there is a better profit element to the left or to the right.

while num_people_max > 0:
    max_price = max(prices) #TBD .. check if i can do it without using max function everytime ... 

    if max_price == 0:
        break
    max_p += max_price
    prices[prices.index(max_price)] -= 1
    num_people_max -= 1
    
print(max_p , min_p)
    

