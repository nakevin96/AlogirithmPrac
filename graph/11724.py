# 연결 요소의 갯수 : https://www.acmicpc.net/problem/11724
import sys

input = sys.stdin.readline
N, M = map(int, input().split(' '))
edge_list = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split(' '))
    edge_list[v1].append(v2)
    edge_list[v2].append(v1)

result = 0
for v in range(1, N + 1):
    if visited[v] == 0:
        result += 1
        visited[v] = 1
        stack = [v]
        while stack:
            curr_v = stack.pop()
            for next_v in edge_list[curr_v]:
                if visited[next_v] == 0:
                    visited[next_v] = 1
                    stack.append(next_v)
print(result)
