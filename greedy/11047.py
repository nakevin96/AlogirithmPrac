import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, K = map(int, input().split(" "))
coins = [0]
for _ in range(N):
    coins.append(int(input()))
coins.sort()

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for coin_idx in range(1, N + 1):
    for money in range(1, K + 1):
        coin = coins[coin_idx]
        if money < coin:
            dp[coin_idx][money] = dp[coin_idx - 1][money]
        else:
            if dp[coin_idx - 1][money] == 0:
                if money % coin == 0:
                    dp[coin_idx][money] = money // coin
                else:
                    dp[coin_idx][money] = dp[coin_idx-1][money]
            else:
                dp[coin_idx][money] = min(dp[coin_idx - 1][money % coin] + (money // coin), dp[coin_idx - 1][money])

print(dp[N][K])
