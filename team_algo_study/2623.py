from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline

singer_num, pd_num = map(int, input().split(' '))

in_count = [0 for _ in range(singer_num + 1)]
in_count[0] = -1

connect_info = [[] for _ in range(singer_num + 1)]

for _ in range(pd_num):
    pick_list = list(map(int, input().split(' ')))
    for prev_singer, next_singer in combinations(pick_list[1:], 2):
        in_count[next_singer] += 1
        connect_info[prev_singer].append(next_singer)

result = []
queue = deque([idx for idx, val in enumerate(in_count) if val == 0])

while queue:
    curr_singer = queue.popleft()
    result.append(curr_singer)

    for next_singer in connect_info[curr_singer]:
        in_count[next_singer] -= 1
        if in_count[next_singer] == 0:
            queue.append(next_singer)

if sum(in_count) >= 0:
    print(0)
else:
    for r in result:
        print(r)
