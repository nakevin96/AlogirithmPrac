# 다이아몬드 광산: https://www.acmicpc.net/problem/1028
import sys
import pprint

input = sys.stdin.readline

R, C = map(int, input().split(' '))
map_info = []
for r in range(R):
    map_info.append(list(map(int, list(input().rstrip()))))

dp_dr = [[0 for _ in range(C)] for _ in range(R)]
dp_dl = [[0 for _ in range(C)] for _ in range(R)]
dp_ur = [[0 for _ in range(C)] for _ in range(R)]
dp_ul = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R - 1, -1, -1):
    for c in range(C):
        if map_info[r][c] == 1:
            if r == R - 1:
                dp_dr[r][c] = 1
                dp_dl[r][c] = 1
            else:
                dp_dr[r][c] = dp_dr[r + 1][c + 1] + 1 if c + 1 <= C - 1 else 1
                dp_dl[r][c] = dp_dl[r + 1][c - 1] + 1 if c - 1 >= 0 else 1

result = 0
for r in range(R):
    for c in range(C):
        tmp_size = min(dp_dr[r][c], dp_dl[r][c])
        for size in range(tmp_size, 0, -1):
            if size <= result:
                break
            point_r = r + size - 1
            if point_r >= R:
                continue
            left_point_c, right_point_c = c - size + 1, c + size - 1
            if left_point_c < 0 or right_point_c >= C:
                continue
            if dp_dr[point_r][left_point_c] >= size and dp_dl[point_r][right_point_c] >= size:
                result = size

print(result)
