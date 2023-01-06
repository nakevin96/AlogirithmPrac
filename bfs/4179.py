'''
지훈이는 미로에서 일을 한다
미로에서 지훈이의 위치와 불이 난 위치를 감안해 불에 타지 않고 탈출을 얼마나 빨리 할 수 있는지 구해라
지훈이와 불은 수직 수평으로만 이동가능하다
#: 벽
. : 지나갈 수 있는 공간
J : 지훈이 위치
F: 불이난 공간
'''
from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().rstrip().split(" "))
visited = [[0 for _ in range(c)] for _ in range(r)]
maze_info = []
peoples = []
fires = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _r in range(r):
    maze_info.append(list(stdin.readline().rstrip()))
    for _c in range(c):
        if maze_info[_r][_c] == "F":
            fires.append([_r, _c, -1])
        elif maze_info[_r][_c] == "J":
            peoples.append([_r, _c, 1])
        elif maze_info[_r][_c] == "#":
            visited[_r][_c] = 1

queue = deque()
for f in fires:
    queue.append(f)
for p in peoples:
    queue.append(p)

result = "IMPOSSIBLE"
while queue:
    curr_r, curr_c, curr_val = queue.popleft()
    if visited[curr_r][curr_c] == 1:
        continue
    visited[curr_r][curr_c] = 1
    if curr_val >= 1 and (curr_r == 0 or curr_c == 0 or curr_r == r - 1 or curr_c == c - 1):
        result = curr_val
        break
    for i in range(4):
        nr = curr_r + dr[i]
        nc = curr_c + dc[i]
        if nr < 0 or nc < 0 or nr >= r or nc >= c:
            continue
        if visited[nr][nc] == 0:
            if curr_val == -1:
                queue.append([nr, nc, -1])
            else:
                queue.append([nr, nc, curr_val + 1])

print(result)
