s = input()

char_len = len(s)
zeros = 0
single_zeros = 0
others = 0

i = 0
while i < char_len:
    if s[i] != '0' :
        others += 1
    elif s[i] == '0' :
        if i+1 < char_len and s[i+1] == '0':
            zeros += 2
            i += 1
        else:
            single_zeros += 1
    i+=1


print(others+single_zeros+zeros//2+zeros%2)

