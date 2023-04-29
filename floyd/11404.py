# 플로이드 : https://www.acmicpc.net/problem/11404
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
map_info = [[float('inf') for _ in range(n)] for _ in range(n)]
for node in range(n):
    map_info[node][node] = 0
for _ in range(m):
    a, b, c = map(int, input().rstrip().split(' '))
    map_info[a-1][b-1] = min(map_info[a-1][b-1], c)


for target_node in range(n):
    for r in range(n):
        for c in range(n):
            if map_info[r][c] > map_info[r][target_node] + map_info[target_node][c]:
                map_info[r][c] = map_info[r][target_node] + map_info[target_node][c]

for r in range(n):
    print_list = []
    for c in range(n):
        if map_info[r][c] == float('inf'):
            print_list.append('0')
        else:
            print_list.append(str(map_info[r][c]))
    print(' '.join(print_list))
