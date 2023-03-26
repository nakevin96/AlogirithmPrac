# https://www.acmicpc.net/problem/15988
import sys

input = sys.stdin.readline

T = int(input())
dp = [-1 for _ in range(1000005)]
dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 4

for i in range(4, 1000004):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for _ in range(T):
    n = int(input())
    print(dp[n])
