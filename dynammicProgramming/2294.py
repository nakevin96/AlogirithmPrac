# 동전 2 : https://www.acmicpc.net/problem/2294
import sys

input = sys.stdin.readline
n, k = map(int, input().split(' '))
# dp는 해당 금액을 낼수 있는 동전조합이 존재할 때 내야하는 최소 동전 수
dp = [-1 for _ in range(k + 1)]
dp[0] = 0

for _ in range(n):
    coin = int(input())
    for m in range(coin, k + 1):
        if dp[m - coin] >= 0:
            if dp[m] == -1:
                dp[m] = dp[m - coin] + 1
            else:
                dp[m] = min(dp[m], dp[m - coin] + 1)
print(dp[k])
