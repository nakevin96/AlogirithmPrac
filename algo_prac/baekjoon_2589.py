from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
row_len, col_len = map(int, input().split())
map_detail = []
for _ in range(row_len):
    map_detail.append(input())


def bfs(_row_idx, _col_idx):
    visited = [[0 for _c in range(col_len)] for _r in range(row_len)]
    queue = deque()
    queue.append((_row_idx, _col_idx))
    visited[_row_idx][_col_idx] = 1
    count = 0
    while queue:
        curr_point = queue.popleft()
        for i in range(4):
            next_row = curr_point[0] + dx[i]
            next_col = curr_point[1] + dy[i]
            if next_row < 0 or next_row >= row_len or next_col < 0 or next_col >= col_len:
                continue
            elif map_detail[next_row][next_col] == 'L' and visited[next_row][next_col] == 0:
                visited[next_row][next_col] = visited[curr_point[0]][curr_point[1]] + 1
                count = max(count, visited[next_row][next_col])
                queue.append((next_row, next_col))
    return count-1


result = 0
for row_idx in range(row_len):
    for col_idx in range(col_len):
        if map_detail[row_idx][col_idx] == 'L':
            result = max(result, bfs(row_idx, col_idx))

print(result)
