from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split(" "))

total_list = deque([i for i in range(1, n+1)])
answer = 0
find_list = list(map(int, stdin.readline().rstrip().split(" ")))

for f in find_list:
    f_idx = total_list.index(f)
    while total_list[0] != f:
        if f_idx < len(total_list) - f_idx:
            total_list.append(total_list.popleft())
        else:
            total_list.appendleft(total_list.pop())
        answer += 1
    total_list.popleft()

print(answer)
