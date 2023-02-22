from collections import deque
from itertools import permutations

direction = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
stair_candidates = list(permutations([0, 1, 2, 3, 4], 5))


def rotate_matrix(matrix, rotate_num):
    if rotate_num == 0:
        return matrix
    r_len, c_len = len(matrix), len(matrix[0])
    for _ in range(rotate_num):
        new_matrix = [[0 for _ in range(c_len)] for _ in range(r_len)]
        for mr in range(r_len):
            for mc in range(c_len):
                new_matrix[c_len - mc - 1][mr] = matrix[mr][mc]
        matrix = new_matrix
    return matrix


def bfs(maze):
    if maze[0][0][0] == 0 or maze[4][4][4] == 0:
        return -1
    visited = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    queue = deque([(0, 0, 0, 0)])
    visited[0][0][0] = 1
    while queue:
        cr, cc, ch, step = queue.popleft()
        if cr == 4 and cc == 4 and ch == 4:
            return step
        for dr, dc, dh in direction:
            nr, nc, nh = cr + dr, cc + dc, ch + dh
            if nr < 0 or nc < 0 or nh < 0 or nr >= 5 or nc >= 5 or nh >= 5:
                continue
            if visited[nr][nc][nh] == 0 and maze[nr][nc][nh] == 1:
                visited[nr][nc][nh] = 1
                queue.append((nr, nc, nh, step + 1))
    return -1


matrix_list = []
for m in range(5):
    tmp_matrix = []
    for _ in range(5):
        tmp_matrix.append(list(map(int, input().split(" "))))
    matrix_list.append(tmp_matrix)

result = -1
for k in range(1024):
    divided_num = k
    rotate_list = []
    for _ in range(5):
        rotate_list.append(divided_num % 4)
        divided_num = divided_num // 4
    maze = [rotate_matrix(matrix_list[i], rotate_list[i]) for i in range(5)]
    for stair_candidate in stair_candidates:
        stair_maze = []
        for stair in stair_candidate:
            stair_maze.append(maze[stair])
        tmp_result = bfs(stair_maze)
        if result == -1:
            result = tmp_result
        elif tmp_result == -1:
            continue
        else:
            result = min(result, tmp_result)

print(result)
