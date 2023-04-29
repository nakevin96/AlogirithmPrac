# 플로이드 2: https://www.acmicpc.net/problem/11780
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
map_info = [[float('inf') for _ in range(n)] for _ in range(n)]
for r in range(n):
    map_info[r][r] = 0
next_info = [[-1 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split(' '))
    if c < map_info[a - 1][b - 1]:
        map_info[a - 1][b - 1] = c
        next_info[a - 1][b - 1] = b - 1

for target_node in range(n):
    for r in range(n):
        for c in range(n):
            if map_info[r][c] > map_info[r][target_node] + map_info[target_node][c]:
                map_info[r][c] = map_info[r][target_node] + map_info[target_node][c]
                next_info[r][c] = next_info[r][target_node]

path_list = []

for r in range(n):
    print_list = []
    for c in range(n):
        if map_info[r][c] == float('inf'):
            print_list.append('0')
            path_list.append(['0'])
        else:
            print_list.append(str(map_info[r][c]))
            if map_info[r][c] > 0:
                tmp_path = [str(r + 1)]
                start = r
                while next_info[start][c] != c:
                    tmp_path.append(str(next_info[start][c] + 1))
                    start = next_info[start][c]
                tmp_path.append(str(c + 1))
                path_list.append(tmp_path)
            else:
                path_list.append(['0'])
    print(' '.join(print_list))

for path in path_list:
    if len(path) == 1:
        print('0')
    else:
        print(str(len(path)) + ' ' + ' '.join(path))
