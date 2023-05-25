from sys import stdin

input = stdin.readline

n, k = map(int, input().split(' '))
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for coin in coins:
    for money in range(coin, k + 1):
        dp[money] += dp[money - coin]
print(dp[k])
