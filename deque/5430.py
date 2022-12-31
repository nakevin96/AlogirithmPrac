from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    p = list(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    arr = deque(stdin.readline().rstrip()[1:-1].split(","))
    if n == 0:
        arr = deque()

    is_left = True
    flag = False
    for _p in p:
        if _p == "R":
            is_left = not is_left
        elif _p == "D":
            if len(arr) == 0:
                print("error")
                flag = True
                break
            if is_left:
                arr.popleft()
            else:
                arr.pop()

    if not flag:
        print("[" + ",".join(arr) + "]" if is_left else "[" + ",".join(reversed(arr)) + "]")
