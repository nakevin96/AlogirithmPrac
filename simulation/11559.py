# https://www.acmicpc.net/problem/11559
from collections import deque

R, C = 12, 6
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
field_info = []
for _ in range(R):
    field_info.append(list(input()))


def get_connect_num(sr, sc, color):
    connect_result = 0
    visited = [[0 for _c in range(C)] for _r in range(R)]
    visited[sr][sc] = 1
    queue = deque([(sr, sc, 1)])
    while queue:
        cr, cc, count = queue.popleft()
        connect_result += 1
        for di in range(4):
            nr, nc = cr + direction[di][0], cc + direction[di][1]
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if visited[nr][nc] == 0 and field_info[nr][nc] == color:
                visited[nr][nc] = 1
                queue.append((nr, nc, count + 1))
    return connect_result


def explode_puyo(er, ec, color):
    field_info[er][ec] = "."
    queue = deque([(er, ec)])
    while queue:
        cr, cc = queue.popleft()
        for di in range(4):
            nr, nc = cr + direction[di][0], cc + direction[di][1]
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if field_info[nr][nc] == color:
                field_info[nr][nc] = "."
                queue.append((nr, nc))


def refresh_field():
    for c_idx in range(C):
        tmp_row_info = ["." for _ in range(R)]
        tmp_idx = R - 1
        for r_idx in range(R - 1, -1, -1):
            if field_info[r_idx][c_idx] != ".":
                tmp_row_info[tmp_idx] = field_info[r_idx][c_idx]
                tmp_idx -= 1
        for r_idx in range(R):
            field_info[r_idx][c_idx] = tmp_row_info[r_idx]


result = 0
while True:
    is_done = True
    for r in range(R):
        for c in range(C):
            if field_info[r][c] != ".":
                connect_num = get_connect_num(r, c, field_info[r][c])
                if connect_num >= 4:
                    is_done = False
                    explode_puyo(r, c, field_info[r][c])
    if is_done:
        break
    else:
        result += 1
        refresh_field()

print(result)
