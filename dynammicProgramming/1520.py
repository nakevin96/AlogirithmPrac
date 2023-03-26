# 내리막길: https://www.acmicpc.net/problem/1520
import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

R, C = map(int, input().split(' '))
map_info = []
visited = [[-1 for _ in range(C)] for _ in range(R)]
visited[R - 1][C - 1] = 1
for _ in range(R):
    map_info.append(list(map(int, input().split(' '))))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def sol(sr, sc):
    if visited[sr][sc] == -1:
        visited[sr][sc] = 0
        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if map_info[nr][nc] < map_info[sr][sc]:
                visited[sr][sc] += sol(nr, nc)

    return visited[sr][sc]


print(sol(0, 0))
