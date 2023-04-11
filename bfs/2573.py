from sys import stdin

input = stdin.readline

N, M = map(int, input().strip().split(' '))
map_info = []
for n in range(N):
    map_info.append(list(map(int, input().strip().split(' '))))

result = 0
while True:
    result += 1
    check_info = [[0 for _ in range(M)] for _ in range(N)]
    is_break = False
    is_empty = True
    for r in range(N):
        for c in range(M):
            if map_info[r][c] > 0:
                is_empty = False
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= N or nc >= M:
                        continue
                    if map_info[nr][nc] == 0:
                        check_info[r][c] += 1
    if is_empty:
        print(0)
        break
    count = 0
    check_point = [0, 0]
    for r in range(N):
        for c in range(M):
            map_info[r][c] -= check_info[r][c]
            if map_info[r][c] <= 0:
                map_info[r][c] = 0
            else:
                count += 1
                check_point = [r, c]
    if count == 0:
        print(0)
        break

    check_info = [[0 for _ in range(M)] for _ in range(N)]
    check_info[check_point[0]][check_point[1]] = 1
    stack = [(check_point[0], check_point[1])]
    tmp_count = 1
    while stack:
        cr, cc = stack.pop()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if map_info[nr][nc] > 0 and check_info[nr][nc] == 0:
                check_info[nr][nc] = 1
                tmp_count += 1
                stack.append((nr, nc))
    if tmp_count != count:
        print(result)
        break
