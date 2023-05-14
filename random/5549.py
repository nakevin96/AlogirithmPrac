# 행성 탐사
import sys
from pprint import pprint

input = sys.stdin.readline

R, C = map(int, input().split(' '))
K = int(input())

terrain = [[[0 for _ in range(3)] for _ in range(C + 1)] for _ in range(R + 1)]
for r in range(1, R + 1):
    tmp_list = list(input().rstrip())
    for c in range(1, C + 1):
        terrain[r][c][0] = terrain[r][c - 1][0]
        terrain[r][c][1] = terrain[r][c - 1][1]
        terrain[r][c][2] = terrain[r][c - 1][2]
        if tmp_list[c - 1] == 'J':
            terrain[r][c][0] += 1
        elif tmp_list[c - 1] == 'O':
            terrain[r][c][1] += 1
        elif tmp_list[c - 1] == 'I':
            terrain[r][c][2] += 1
        else:
            print('error')
    for c in range(1, C+1):
        terrain[r][c][0] += terrain[r - 1][c][0]
        terrain[r][c][1] += terrain[r - 1][c][1]
        terrain[r][c][2] += terrain[r - 1][c][2]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split(' '))
    result = [str(terrain[x2][y2][0] - terrain[x1 - 1][y2][0] - terrain[x2][y1 - 1][0] + terrain[x1 - 1][y1 - 1][0]),
              str(terrain[x2][y2][1] - terrain[x1 - 1][y2][1] - terrain[x2][y1 - 1][1] + terrain[x1 - 1][y1 - 1][1]),
              str(terrain[x2][y2][2] - terrain[x1 - 1][y2][2] - terrain[x2][y1 - 1][2] + terrain[x1 - 1][y1 - 1][2])]
    print(' '.join(result))
