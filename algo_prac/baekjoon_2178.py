from collections import deque

row_len, col_len = map(int, input().split())

map_info = []
for i in range(row_len):
    map_info.append(list(map(int, list(input()))))
visited = [[0 for _c in range(col_len)] for _r in range(row_len)]
queue = deque()
queue.append((0, 0))
visited[0][0] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    curr_point = queue.popleft()
    for move_idx in range(4):
        next_row = curr_point[0] + dx[move_idx]
        next_col = curr_point[1] + dy[move_idx]
        if next_row < 0 or next_row >= row_len or next_col < 0 or next_col >= col_len:
            continue
        elif map_info[next_row][next_col] == 1 and visited[next_row][next_col] == 0:
            visited[next_row][next_col] = visited[curr_point[0]][curr_point[1]] + 1
            queue.append((next_row, next_col))

print(visited[row_len-1][col_len-1])
