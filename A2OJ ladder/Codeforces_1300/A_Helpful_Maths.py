input_nos = [int(x) for x in input().split("+")]

ones = ""
twos = ""
threes = ""



for num in input_nos:
    if num == 1 :
        ones += "1"
        ones += "+"
    elif num ==2 :
        twos += "2"
        twos += "+"
    elif num == 3:
        threes += "3"
        threes += "+"


print ( (ones+twos+threes)[0:-1] )

