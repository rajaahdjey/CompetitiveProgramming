num_words = int(input())

for word in range(num_words):
    input_text = input()
    if len(input_text) <= 10:
        print(input_text)
    else:
        print(input_text[0]+str(len(input_text)-2)+input_text[-1])