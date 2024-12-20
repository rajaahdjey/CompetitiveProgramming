input_number = int(input())

fib_dict = {0:0,1:1}


for i in range(input_number+2):
    if i in fib_dict:
        continue
    fib_dict[i] = fib_dict[i-2]+fib_dict[i-1]
    if fib_dict[i] == input_number:
        break

if input_number == 0:
    print(0, 0, 0)
elif input_number == 1:
    print(0 , 0, 1)
elif input_number == 2:
    print(0, 1, 1)
else:
    print(fib_dict[i-4] , fib_dict[i-3] , fib_dict[i-1]  )