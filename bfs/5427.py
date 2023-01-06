'''
상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다
건물 일부에는 불이 났고 상근이는 출구를 향해 뛰고 있다
벽에는 불이 붙지 않으며 동서남북으로 불이 퍼진다 불이 옮겨진 칸 혹인 이제 불이 붙으려는 칸으로 이동은 불가능 하다
최대한 빨리 탈출할 수 있는 시간을 구해라
'''

from sys import stdin
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def solution():
    c, r = map(int, stdin.readline().rstrip().split(" "))
    info = []
    visited = [[0 for _c in range(c)] for _r in range(r)]
    queue = deque()
    start = []
    for _r in range(r):
        info.append(list(stdin.readline().rstrip()))
        for _c in range(c):
            if info[_r][_c] == "*":
                queue.append((_r, _c, -1))
            elif info[_r][_c] == "@":
                start.append((_r, _c, 1))
            elif info[_r][_c] == "#":
                visited[_r][_c] = 1
    queue.append(start[0])

    while queue:
        curr_r, curr_c, time = queue.popleft()
        if visited[curr_r][curr_c] == 1:
            continue
        visited[curr_r][curr_c] = 1

        if time >= 1 and (curr_r == 0 or curr_c == 0 or curr_r == r - 1 or curr_c == c - 1):
            return time

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue
            if visited[nr][nc] == 0:
                if time == -1:
                    queue.append((nr, nc, -1))
                else:
                    queue.append((nr, nc, time + 1))
    return "IMPOSSIBLE"


t = int(stdin.readline().rstrip())
for _ in range(t):
    print(solution())
