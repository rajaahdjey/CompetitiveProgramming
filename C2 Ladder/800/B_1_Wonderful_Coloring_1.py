t = int(input())


for _ in range(t):
    word = input()
    letters = dict()
    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    unique_letters = 0
    double_letters = 0
    triple_or_more_letters = 0
    for letter in letters:
        if letters[letter] == 1:
            unique_letters += 1 
        elif letters[letter] == 2:
            double_letters += 1
        else:
            triple_or_more_letters += 1

    print(unique_letters//2 + double_letters + triple_or_more_letters)


