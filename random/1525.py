# 퍼즐 : https://www.acmicpc.net/problem/1525
import sys
from collections import deque

input = sys.stdin.readline

finished_map = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
map_info = ''
for _ in range(3):
    map_info += ''.join(list(input().rstrip().split(' ')))


def bfs(start_map_string):
    visited = {start_map_string: 0}
    queue = deque([start_map_string])
    while queue:
        map_string = queue.popleft()
        curr_val = visited[map_string]
        if map_string == '123456780':
            return curr_val

        zero_idx = map_string.index('0')
        zero_row, zero_col = zero_idx // 3, zero_idx % 3

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = zero_row + dr, zero_col + dc
            if nr < 0 or nc < 0 or nr >= 3 or nc >= 3:
                continue
            next_zero_idx = (3 * nr) + nc
            map_list = list(map_string)
            map_list[zero_idx], map_list[next_zero_idx] = map_list[next_zero_idx], map_list[zero_idx]
            new_map_string = ''.join(map_list)

            if new_map_string not in visited:
                visited[new_map_string] = curr_val+1
                queue.append(new_map_string)
    return -1

print(bfs(map_info))
