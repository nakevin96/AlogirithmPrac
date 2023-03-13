# 가장 큰 증가하는 부분 수열 : https://www.acmicpc.net/problem/11055
n = int(input())
n_list = list(map(int, input().split(' ')))
dp = [0 for _ in range(n)]
dp[0] = n_list[0]
for check in range(1, n):
    pre_max = 0
    for pre_check in range(check, -1, -1):
        if n_list[pre_check] < n_list[check]:
            pre_max = max(dp[pre_check], pre_max)
    dp[check] = pre_max + n_list[check]
print(max(dp))
