encoded = input()
ans = ""
i = 0
#print(encoded[i-2:i])
while i < len(encoded):
    if encoded[i:i+2] == "--" :
        ans += "2"
        i += 2
    elif encoded[i:i+2] == "-." :
        ans += "1"
        i += 2
    else:
        ans += "0"
        i += 1
print(ans) 