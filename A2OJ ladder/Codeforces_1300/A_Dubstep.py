before = input()

end = len(before)

final_string = ""
prev_char = ""

while end >= 0:
    # print(end)
    # print(before[end-3:end])
    if before[end-3:end] == "WUB":
        if final_string != "" and prev_char != " ":
            final_string = " " + final_string
            prev_char = " "
        else:
            prev_char = ""
        end = end-3
    else:
        final_string = before[end-1:end]+final_string
        prev_char = ""
        end -= 1

print(final_string.lstrip().rstrip())
        

