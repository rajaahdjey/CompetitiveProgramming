s = input()
t = input()

if len(s) > len(t):
    long_string = s
    long_len = len(s)
    short_string = t
    short_len = len(t)
else:
    short_string = s
    short_len = len(s)
    long_string = t
    long_len = len(t)

dp = [""]*(short_len+1)

print(short_string,short_len,long_string,long_len)

longest_idx = 0
j = 0
for i in range(0,short_len):
    print(i)
    j = longest_idx
    while (j < long_len):
        print(j)
        print(short_string[i],long_string[j])
        if short_string[i] == long_string[j]:
            dp[i+1] = dp[i] + long_string[j]
            print(dp)
            longest_idx = j+1
            j += 1
            break
        else:
            dp[i+1] = dp[i]
            j += 1
print(dp[-1])
    