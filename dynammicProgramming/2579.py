# 계단 오르기: https://www.acmicpc.net/problem/2579
import sys

input = sys.stdin.readline

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))

if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[1] + stairs[2])
else:
    dp = [[0 for _ in range(N + 1)] for _ in range(2)]

    dp[0][1] = stairs[1]
    dp[0][2], dp[1][2] = stairs[1] + stairs[2], stairs[2]
    for i in range(3, N + 1):
        # 바로 앞 계단
        dp[0][i] = dp[1][i - 1] + stairs[i]
        dp[1][i] = max(dp[0][i - 2], dp[1][i - 2]) + stairs[i]

    print(max(dp[0][N], dp[1][N]))
