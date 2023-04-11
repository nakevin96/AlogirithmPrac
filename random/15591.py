# MooTube (Silver) : https://www.acmicpc.net/problem/15591

# 농부 존은 남는 시간에 MooTube라는 동영상 공유 서비스를 만들었다.
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
N, Q = map(int, input().rstrip().split(' '))
map_info = defaultdict(list)
for _ in range(N - 1):
    p, q, r = map(int, input().rstrip().split(' '))
    map_info[p].append((q, r))
    map_info[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().strip().split(' '))
    visited = [False for _ in range(N+1)]
    visited[v] = True
    queue = deque([(v, 1000000001)])
    result = 0
    while queue:
        curr_node, curr_k = queue.popleft()
        if curr_k >= k:
            result += 1
        for next_node, next_cost in map_info[curr_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, min(curr_k, next_cost)))
    print(result - 1)
