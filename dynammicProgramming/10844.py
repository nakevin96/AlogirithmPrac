# 쉬운 계단 수: https://www.acmicpc.net/problem/10844
N = int(input())
dp = [[0 for _ in range(12)] for _ in range(N)]
dp[0] = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
for i in range(1, N):
    for idx in range(1, 11):
        dp[i][idx] = (dp[i - 1][idx - 1] + dp[i - 1][idx + 1]) % 1000000000

print(sum(dp[N - 1]) % 1000000000)
