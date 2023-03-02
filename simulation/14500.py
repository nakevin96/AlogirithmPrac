# techromino_list = [
#     [[1, 1, 1, 1]],
#     [[1],
#      [1],
#      [1],
#      [1]],
#     [[1, 1],
#      [1, 1]],
#     [[1, 0],
#      [1, 0],
#      [1, 1]],
#     [[0, 1],
#      [0, 1],
#      [1, 1]],
#     [[1, 1, 1],
#      [1, 0, 0]],
#     [[1, 1, 1],
#      [0, 0, 1]],
#     [[1, 1],
#      [0, 1],
#      [0, 1]],
#     [[1, 1],
#      [1, 0],
#      [1, 0]],
#     [[0, 0, 1],
#      [1, 1, 1]],
#     [[1, 0, 0],
#      [1, 1, 1]],
#     [[1, 0],
#      [1, 1],
#      [0, 1]],
#     [[0, 1],
#      [1, 1],
#      [1, 0]],
#     [[0, 1, 1],
#      [1, 1, 0]],
#     [[1, 1, 0],
#      [0, 1, 1]],
#     [[1, 1, 1],
#      [0, 1, 0]],
#     [[0, 1],
#      [1, 1],
#      [0, 1]],
#     [[0, 1, 0],
#      [1, 1, 1]],
#     [[1, 0],
#      [1, 1],
#      [1, 0]],
# ]
#
# R, C = map(int, input().split(" "))
# map_info = []
# result = 0
# for _ in range(R):
#     map_info.append(list(map(int, input().split(" "))))
# for tech in techromino_list:
#     tech_r_len, tech_c_len = len(tech), len(tech[0])
#     for sr in range(R-tech_r_len+1):
#         for sc in range(C-tech_c_len+1):
#             tmp_sum = 0
#             for tr in range(tech_r_len):
#                 for tc in range(tech_c_len):
#                     tmp_sum += (map_info[sr+tr][sc+tc] * tech[tr][tc])
#             result = max(result, tmp_sum)
# print(result)
#

import sys

sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split(' '))
map_info = []
max_num = 0
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _n in range(N):
    map_info.append(list(map(int, input().split(' '))))
    max_num = max(max_num, max(map_info[_n]))

result = 0
visited = set()


def dfs(cr, cc, sum_val):
    global result
    if sum_val + (max_num * (4 - len(visited))) < result:
        return

    if len(visited) == 4:
        tmp_result = 0
        for sr, sc in visited:
            tmp_result += map_info[sr][sc]
        result = max(result, tmp_result)
        return
    for i in range(4):
        nr, nc = cr + direction[i][0], cc + direction[i][1]
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue
        if (nr, nc) not in visited:
            visited.add((nr, nc))
            if len(visited) == 3:
                dfs(cr, cc, sum_val + map_info[nr][nc])
            dfs(nr, nc, sum_val + map_info[nr][nc])
            visited.remove((nr, nc))


for n in range(N):
    for m in range(M):
        visited.add((n, m))
        dfs(n, m, map_info[n][m])
        visited.remove((n, m))
print(result)

