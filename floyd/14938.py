# 서강 그라운드: https://www.acmicpc.net/problem/14938
import sys

input = sys.stdin.readline

n, m, r = map(int, input().strip().split(' '))
item_list = list(map(int, input().strip().split(' ')))

map_info = [[float('inf') for _ in range(n)] for _ in range(n)]
for v in range(n):
    map_info[v][v] = 0
for _ in range(r):
    v1, v2, dist = map(int, input().strip().split(' '))
    map_info[v1-1][v2-1] = dist
    map_info[v2-1][v1-1] = dist

for target_area in range(n):
    for r in range(n):
        for c in range(n):
            if map_info[r][c] > map_info[r][target_area] + map_info[target_area][c]:
                map_info[r][c] = map_info[r][target_area] + map_info[target_area][c]

result = 0
for target_area in range(n):
    tmp_result = 0
    for move_area in range(n):
        if map_info[target_area][move_area] <= m:
            tmp_result += item_list[move_area]
    if result < tmp_result:
        result = tmp_result
print(result)
