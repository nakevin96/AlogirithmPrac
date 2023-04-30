# 운동: https://www.acmicpc.net/problem/1956
import sys

input = sys.stdin.readline
INF = float('inf')
V, E = map(int, input().split(' '))
map_info = [[INF for _ in range(V)] for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split(' '))
    map_info[a - 1][b - 1] = c

for mid_v in range(V):
    for start_v in range(V):
        for end_v in range(V):
            if map_info[start_v][end_v] > map_info[start_v][mid_v] + map_info[mid_v][end_v]:
                map_info[start_v][end_v] = map_info[start_v][mid_v] + map_info[mid_v][end_v]

result = INF
for start_v in range(V):
    for end_v in range(V):
        if result > map_info[start_v][end_v] + map_info[end_v][start_v]:
            result = map_info[start_v][end_v] + map_info[end_v][start_v]

if result == INF:
    print('-1')
else:
    print(result)
