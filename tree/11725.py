# 트리의 부모 찾기: https://www.acmicpc.net/problem/11725
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
map_info = defaultdict(list)
for _ in range(N - 1):
    v1, v2 = map(int, input().rstrip().split(' '))
    map_info[v1].append(v2)
    map_info[v2].append(v1)

parent = [0 for _ in range(N + 1)]
queue = deque([1])


# while queue:
#     curr_node = queue.popleft()
#     for next_node in map_info[curr_node]:
#         if next_node == parent[curr_node]:
#             continue
#         parent[next_node] = curr_node
#         queue.append(next_node)
#
# for idx in range(2, N+1):
#     print(parent[idx])

def dfs(curr_node):
    for next_node in map_info[curr_node]:
        if next_node == parent[curr_node]:
            continue
        parent[next_node] = curr_node
        dfs(next_node)


dfs(1)
for idx in range(2, N + 1):
    print(parent[idx])
