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


#better solution to use fixed array and not do if x in list which is o(N) every time ... but not mine ... 

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     tasks = [0] * 26  # Fixed-size array for 26 uppercase English letters
#     curr_task = None
#     ok = True
#     for task in input().strip():  # Using strip() to remove newline characters
#         idx = ord(task) - 65  # Map character to index
#         if tasks[idx]:  # Task already seen
#             if curr_task != task:
#                 ok = False
#                 break
#         else:
#             tasks[idx] = 1  # Mark task as seen
#             curr_task = task
#     print("YES" if ok else "NO")
