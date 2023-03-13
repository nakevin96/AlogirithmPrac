# 동전 : https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coin_list = list(map(int, input().split(' ')))
    target_money = int(input())

    dp = [0 for _ in range(target_money+1)]
    dp[0] = 1
    for coin in coin_list:
        for money in range(coin, target_money+1):
            dp[money] += dp[money-coin]
    print(dp[target_money])
