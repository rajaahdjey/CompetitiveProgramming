init_string = input()

vowels = {'A','a','O','o','Y','y','E','e','U','u','I','i'}

final_string = ""

for letter in init_string:
    if letter in vowels:
        continue
    else:
        final_string += "."
        final_string += letter.lower()

print(final_string)