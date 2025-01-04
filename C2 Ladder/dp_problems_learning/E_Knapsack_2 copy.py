N , W = [int(x) for x in input().split()]

values = [0]*(N+1)
weights = [0]*(N+1)

values[0] = 0
weights[0] = 0

for i in range(1,N+1):
    weight , value = [int(x) for x in input().split()]
    #at every i , i can decide to take it , leave it or swap it.
    if weights[i-1] + weight <= W:
        values[i] = values[i-1]+value
        weights[i] = weights[i-1] + weight
    elif value > min(values):
        for j in range(1,i+1):
            print((weight + weights[i-1] - weights[j]) <= W)
            if (values[j] < value) and ((weight + weights[i-1] - weights[j]) <= W):
                print(values,weights)
                values[i] = values[i-1]+value-values[j]
                weights[i] = weights[i-1] + weight -weights[j]
                print(values,weights)
    else:
        values[i] = values[i-1]
        weights[i] = weights[i-1]

    print(values)