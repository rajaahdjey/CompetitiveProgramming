name = input()
name+= input()
letters_available = input()

total_needed = len(name)
missing_extra_count = 0

for letter in letters_available:
    if letter in name:
        name = name.replace(letter,"",1)
        total_needed -= 1
    else:
        missing_extra_count += 1

if total_needed == 0 and missing_extra_count == 0:
    print('YES')
else:
    print("NO")