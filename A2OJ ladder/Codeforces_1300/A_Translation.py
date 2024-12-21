input_text = input()
reversed_text = input()

chk = "YES"

if len(input_text) != len(reversed_text):
    chk = "NO"
else:
    for i in range(len(input_text)):
        if input_text[i] != reversed_text[len(input_text)-1-i]:
            chk = "NO"
            break
        else:
            continue
            
print(chk)