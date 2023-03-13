# 연속합: https://www.acmicpc.net/problem/1912
n = int(input())
n_list = list(map(int, input().split(' ')))
dp = [0 for _ in range(n)]
dp[0] = n_list[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1]+n_list[i], n_list[i])
print(max(dp))
