# https://www.acmicpc.net/problem/14502
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(' '))
tmp_result = N * M
map_info = []
zero_list = []
two_list = []
one_count = 0
for n in range(N):
    map_info.append(input().rstrip().split(' '))
    for m in range(M):
        if map_info[n][m] == '0':
            zero_list.append((n, m))
        elif map_info[n][m] == '2':
            two_list.append((n, m))
        else:
            one_count += 1
result = 0

for pos1, pos2, pos3 in combinations(zero_list, 3):
    map_info[pos1[0]][pos1[1]], map_info[pos2[0]][pos2[1]], map_info[pos3[0]][pos3[1]] = '1', '1', '1'
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque()
    for tl_r, tl_c in two_list:
        visited[tl_r][tl_c] = True
        queue.append((tl_r, tl_c))
    test_result = (N * M) - 3 - one_count
    while queue:
        cr, cc = queue.popleft()
        test_result -= 1
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if map_info[nr][nc] == '0' and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))
    if result < test_result:
        result = test_result

    map_info[pos1[0]][pos1[1]], map_info[pos2[0]][pos2[1]], map_info[pos3[0]][pos3[1]] = '0', '0', '0'

print(result)
