contest_count = int(input())

scores = [int(x) for x in input().split(" ")]

#when only one test is taken, min and max are the same
min_score = scores[0]
max_score = scores[0]

best_perf = 0

for score in scores:
    if score > max_score:
        best_perf += 1
        max_score = score
    if score < min_score:
        best_perf += 1 
        min_score = score

print(best_perf)