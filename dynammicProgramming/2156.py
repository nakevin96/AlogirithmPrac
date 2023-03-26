# 포도주 시식: https://www.acmicpc.net/problem/2156
import sys

input = sys.stdin.readline

N = int(input())
wines = [0]
for _ in range(N):
    wines.append(int(input()))

if N == 1:
    print(wines[1])
elif N == 2:
    print(wines[1] + wines[2])
else:
    dp = [[0 for _ in range(N + 1)] for _ in range(3)]
    # dp[0]는 선택 안한거
    # dp[1]은 연달아 선택하지 않은 첫 선택
    # dp[2]는 연달아 2개 선택
    dp[1][1] = wines[1]
    dp[0][2], dp[1][2], dp[2][2] = wines[1], wines[2], wines[1] + wines[2]
    for w in range(3, N+1):
        dp[0][w] = max(dp[0][w-1], dp[1][w-1], dp[2][w-1])
        dp[1][w] = dp[0][w-1] + wines[w]
        dp[2][w] = dp[1][w-1] + wines[w]
    print(max(max(dp[0]), max(dp[1]), max(dp[2])))
