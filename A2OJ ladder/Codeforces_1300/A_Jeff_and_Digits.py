num_cards = int(input())

cards = [int(i) for i in input().split(" ")]

fives = 0
zeros = 0
for card in cards:
    if card == 5:
        fives += 1
    else:
        zeros += 1

if fives >= 9 and zeros > 0:
    final_string = "5"*(9)*int(fives/9)+"0"*zeros
    print(final_string)
elif zeros > 0:
    print(0)
else:
    print(-1)

