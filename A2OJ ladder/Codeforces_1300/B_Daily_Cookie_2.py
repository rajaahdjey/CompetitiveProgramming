N , D = [int(x) for x in input().split(" ")]

S = input()

final_state = ""


for i in range(len(S)):
    if D > 0:
        if S[len(S)-1-i] == "@":
            D = D - 1
        final_state = final_state + "."
    else : 
        final_state = S[:len(S)-i] + final_state
        break

print(final_state)
