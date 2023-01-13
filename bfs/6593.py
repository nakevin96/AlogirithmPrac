'''
빌딩에서 탈출하기 위한 가장 빠른 길을 찾아라
'''
from sys import stdin
from collections import deque

dl = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, stdin.readline().rstrip().split(" "))
    if L == 0 and R == 0 and C == 0:
        break
    building_info = []
    start = []
    end = []
    visited = [[[0 for _c in range(C)] for _r in range(R)] for _l in range(L)]
    for _l in range(L):
        stair_info = []
        for _r in range(R):
            stair_info.append(list(stdin.readline().rstrip()))
            for _c in range(C):
                if stair_info[_r][_c] == "#":
                    visited[_l][_r][_c] = 1
                elif stair_info[_r][_c] == "S":
                    start.append((_l, _r, _c))
                elif stair_info[_r][_c] == "E":
                    end.append((_l, _r, _c))
        stdin.readline().rstrip()
    queue = deque([(start[0][0], start[0][1], start[0][2], 0)])
    is_find = False
    while queue:
        curr_l, curr_r, curr_c, time = queue.popleft()
        if curr_l == end[0][0] and curr_r == end[0][1] and curr_c == end[0][2]:
            is_find = True
            print(f'Escaped in {time}minute(s)')
            break
        if visited[curr_l][curr_r][curr_c] != 0:
            continue
        visited[curr_l][curr_r][curr_c] = 1
        for i in range(6):
            nl = curr_l + dl[i]
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if nl < 0 or nr < 0 or nc < 0 or nl >= L or nr >= R or nc >= C:
                continue
            if visited[nl][nr][nc] == 0:
                queue.append((nl, nr, nc, time + 1))
    if not is_find:
        print("Trapped!")
