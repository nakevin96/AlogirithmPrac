# 1, 2, 3 더하기 : https://www.acmicpc.net/problem/9095
from sys import stdin
input = stdin.readline

T = int(input())
dp = [-1 for _ in range(12)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for idx in range(5, 12):
    dp[idx] = dp[idx-1]+dp[idx-2]+dp[idx-3]

for _ in range(T):
    print(dp[int(input())])
