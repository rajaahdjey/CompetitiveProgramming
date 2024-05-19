n,k,l,c,d,p,nl,np = [int(x) for x in input().split(" ")]

total_drink = k*l

minimum_toasts = int(min(total_drink // nl , c * d , p / np) // n)
print(minimum_toasts)
