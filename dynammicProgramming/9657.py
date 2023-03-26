# 돌 게임: https://www.acmicpc.net/problem/9657
N = int(input())
dp = [-1 for _ in range(1001)]
dp[1], dp[2], dp[3], dp[4] = 1, 0, 1, 1


def sol(num):
    if dp[num] == -1:
        result1 = sol(num - 1)
        result2 = sol(num - 3)
        result3 = sol(num - 4)
        if result1 == 1 and result2 == 1 and result3 == 1:
            dp[num] = 0
        else:
            dp[num] = 1
    return dp[num]


result = sol(N)
print('SK' if result == 1 else 'CY')
