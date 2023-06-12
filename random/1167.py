from sys import stdin
from collections import defaultdict, deque

input = stdin.readline

# V : 정점의 수 [2 : 100_000]
V = int(input())

edge_info = defaultdict(list)
for _ in range(V):
    # dist : 정점 사이의 거리 [1, 10_000]
    dist_info = list(map(int, input().rstrip().split(' ')))
    main_vertex = dist_info[0]
    for other_vertex in range(1, len(dist_info) - 1, 2):
        edge_info[main_vertex].append([dist_info[other_vertex], dist_info[other_vertex + 1]])

queue = deque([[1, 0]])
visited = [-1 for _ in range(V + 1)]
visited[1] = 0
while queue:
    curr_v, curr_val = queue.popleft()

    for next_v, next_val in edge_info[curr_v]:
        if visited[next_v] == -1:
            visited[next_v] = curr_val + next_val
            queue.append([next_v, curr_val + next_val])

max_idx, max_val = -1, -1
for v_idx in range(len(visited)):
    if visited[v_idx] > max_val:
        max_val = visited[v_idx]
        max_idx = v_idx

queue = deque([[max_idx, 0]])
visited = [-1 for _ in range(V + 1)]
visited[max_idx] = 0
while queue:
    curr_v, curr_val = queue.popleft()

    for next_v, next_val in edge_info[curr_v]:
        if visited[next_v] == -1:
            visited[next_v] = curr_val + next_val
            queue.append([next_v, curr_val + next_val])

print(max(visited))
