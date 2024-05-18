s = input()

length = len(s)

lower_ctr = 0

for letter in s:
    if letter.islower():
        lower_ctr += 1
if lower_ctr >= length/2 :
    print(s.lower())
else:
    print(s.upper())
