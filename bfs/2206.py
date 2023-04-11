# 벽 부수고 이동하기: https://www.acmicpc.net/problem/2206
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M = map(int, input().split(' '))
map_info = []
for n in range(N):
    map_info.append(list(map(int, list(input().rstrip()))))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
queue = deque([(0, 0, 0)])
while queue:
    cr, cc, is_crashed = queue.popleft()
    if cr == N - 1 and cc == M - 1:
        break
    for i in range(4):
        nr, nc = cr + direction[i][0], cc + direction[i][1]
        if nr < 0 or nc < 0 or nr >= N or nc >= M or visited[nr][nc][is_crashed] != -1:
            continue
        if map_info[nr][nc] == 0:
            visited[nr][nc][is_crashed] = visited[cr][cc][is_crashed] + 1
            queue.append((nr, nc, is_crashed))
        else:
            if is_crashed == 0:
                visited[nr][nc][is_crashed + 1] = visited[cr][cc][is_crashed] + 1
                queue.append((nr, nc, is_crashed + 1))
print(max(visited[N - 1][M - 1][0], visited[N - 1][M - 1][1]))

# 실패 2
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# visited = [[0 for _ in range(M)] for _ in range(N)]
# result = -1
# broke_count = 0
#
#
# def dfs(dfs_r, dfs_c, dfs_v):
#     global result, broke_count
#     if dfs_r == N - 1 and dfs_c == M - 1:
#         if result == -1:
#             result = dfs_v
#         else:
#             result = min(result, dfs_v)
#         return
#     for i in range(4):
#         nr, nc = dfs_r + dr[i], dfs_c + dc[i]
#         if nr < 0 or nc < 0 or nr >= N or nc >= M or visited[nr][nc] == 1:
#             continue
#         if map_info[nr][nc] == 0:
#             visited[nr][nc] = 1
#             dfs(nr, nc, dfs_v + 1)
#             visited[nr][nc] = 0
#         else:
#             if broke_count == 0:
#                 visited[nr][nc], broke_count = 1, 1
#                 dfs(nr, nc, dfs_v + 1)
#                 visited[nr][nc], broke_count = 0, 0
#
#
# visited[0][0] = 1
# dfs(0, 0, 1)
# print(result)
# 시간 초과
# result = -1
# for cn in range(N):
#     for cm in range(M):
#         if map_info[cn][cm] == 1:
#             tmp_result = -1
#             map_info[cn][cm] = 0
#             visited = [[0 for _ in range(M)] for _ in range(N)]
#             visited[0][0] = 1
#             queue = deque([(0, 0, 1)])
#             while queue:
#                 cr, cc, cv = queue.popleft()
#                 if cr == N - 1 and cc == M - 1:
#                     tmp_result = cv
#                     break
#                 for i in range(4):
#                     nr, nc = cr + dr[i], cc + dc[i]
#                     if nr < 0 or nc < 0 or nr >= N or nc >= M:
#                         continue
#                     if map_info[nr][nc] == 0 and visited[nr][nc] == 0:
#                         visited[nr][nc] = 1
#                         queue.append((nr, nc, cv + 1))
#             if tmp_result > 0:
#                 if result == -1:
#                     result = tmp_result
#                 else:
#                     result = min(result, tmp_result)
#
#             map_info[cn][cm] = 1
# print(result)
