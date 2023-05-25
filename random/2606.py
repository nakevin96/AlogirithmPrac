from sys import stdin
from collections import deque
input= stdin.readline

# computer_num <= 100 자연수 번호 1부터 시작
computer_num = int(input())

network_info = [[] for _ in range(101)]

edge_num = int(input())
for _ in range(edge_num):
    v1, v2 = map(int, input().split(' '))
    network_info[v1].append(v2)
    network_info[v2].append(v1)

visited = [False for _ in range(101)]

queue = deque([1])
visited[1] = True
result = 0
while queue:
    curr_v = queue.popleft()
    for next_v in network_info[curr_v]:
        if not visited[next_v]:
            visited[next_v] = True
            result += 1
            queue.append(next_v)
print(result)