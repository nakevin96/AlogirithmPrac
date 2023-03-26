# 구간합 구하기 5 : https://www.acmicpc.net/problem/11660
import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

map_info = []
dp = [[0 for _ in range(N)] for _ in range(N)]

for r in range(N):
    map_info.append(list(map(int, input().split(' '))))

for r in range(N):
    for c in range(N):
        tmp_sum = map_info[r][c]
        if r - 1 >= 0:
            tmp_sum += dp[r - 1][c]
        if c - 1 >= 0:
            tmp_sum += dp[r][c - 1]
        if r - 1 >= 0 and c - 1 >= 0:
            tmp_sum -= dp[r - 1][c - 1]
        dp[r][c] = tmp_sum


def sol(r1, c1, r2, c2):
    result = dp[r2][c2]
    if r1 - 1 >= 0:
        result -= dp[r1 - 1][c2]
    if c1 - 1 >= 0:
        result -= dp[r2][c1 - 1]
    if r1 - 1 >= 0 and c1 - 1 >= 0:
        result += dp[r1 - 1][c1 - 1]

    return result


for m in range(M):
    x1, y1, x2, y2 = map(int, input().split(' '))
    print(sol(x1 - 1, y1 - 1, x2 - 1, y2 - 1))
