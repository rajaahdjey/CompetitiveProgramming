N , K = [int(x) for x in input().split()]

disliked_digits = set([int(x) for x in input().split()])

allowed_digits = set([i for i in range(1,10)]) - disliked_digits

ans = ""
for digit in str(N):
    if int(digit) in disliked_digits:
        ans += str(int(digit)+1)
        continue
    ans += digit

print(ans)