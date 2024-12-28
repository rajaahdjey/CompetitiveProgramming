for _ in range(int(input())):
    n = int(input())
    s = []
    curr_task = None
    ok = True
    for task in input():
        if task in s and curr_task!= task:
            ok = False
            break
        else:
            curr_task = task
            s.append(task)
    if ok:
        print("YES")
    else:
        print("NO")