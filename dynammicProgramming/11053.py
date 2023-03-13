# 가장 긴 증가하는 부분 수열: https://acmicpc.net/problem/11053
n = int(input())
n_list = list(map(int, input().split(' ')))
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    for pre in range(i):
        if n_list[pre] < n_list[i]:
            dp[i] = max(dp[i], dp[pre])
    dp[i] += 1
print(max(dp))
