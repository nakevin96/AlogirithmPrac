# 퇴사2 : https://www.acmicpc.net/problem/15486
import sys

input = sys.stdin.readline
N = int(input())
time_list = [0 for _ in range(N + 2)]
price_list = [0 for _ in range(N + 2)]
dp = [0 for _ in range(N + 2)]
for idx in range(1, N + 1):
    t, p = map(int, input().split(' '))
    time_list[idx] = t
    price_list[idx] = p

for day in range(N, 0, -1):
    if day + time_list[day] <= N + 1:
        dp[day] = max(dp[day + time_list[day]] + price_list[day], dp[day + 1])
    else:
        dp[day] = dp[day + 1]

print(max(dp))
