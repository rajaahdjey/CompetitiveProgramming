cards = [int(x) for x in input().split()]

card_1 = cards[0]
card_1_ctr = 1
card_2 = None
card_2_ctr = 0
out = True
for card in cards[1:]:
    if card == card_1:
        card_1_ctr += 1
    elif card_2 is None:
        card_2 = card
        card_2_ctr += 1
    elif card == card_2:
        card_2_ctr += 1
    else:
        out = False

if not out:
    print("No")
elif card_1_ctr <= 3 and card_2_ctr <=3:
    if card_1_ctr+card_2_ctr == 4:
        print("Yes")
    else:
        print("No")
else:
    print("No")

