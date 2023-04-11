# 벽부수고 이동하기 2: https://www.acmicpc.net/problem/14442

import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split(' '))
map_info = []
for _ in range(N):
    map_info.append(list(map(int, list(input().rstrip()))))
visited = [[[-1 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs():
    visited[0][0][0] = 1
    queue = deque([(0, 0, 0)])
    while queue:
        cr, cc, cb = queue.popleft()
        if cr == N - 1 and cc == M - 1:
            return visited[cr][cc][cb]
        for i in range(4):
            nr, nc = cr + direction[i][0], cc + direction[i][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= M or visited[nr][nc][cb] != -1:
                continue
            if map_info[nr][nc] == 0:
                visited[nr][nc][cb] = visited[cr][cc][cb] + 1
                queue.append((nr, nc, cb))
            elif cb + 1 <= K and visited[nr][nc][cb+1] == -1:
                visited[nr][nc][cb + 1] = visited[cr][cc][cb] + 1
                queue.append((nr, nc, cb + 1))
    return -1


print(bfs())
