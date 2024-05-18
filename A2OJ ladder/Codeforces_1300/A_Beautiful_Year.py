in_year = input()
condition = True
while condition:
    in_year = str(int(in_year)+1)
    check = []
    for i in range(len(in_year)-1):
        verification = set(in_year[0:i]+in_year[i+1:])
        check.append(in_year[i] in verification)
    if not(any(check)):
        print(in_year)
        break
