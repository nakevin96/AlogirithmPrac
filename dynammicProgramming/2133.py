# 타일 채우기: https://www.acmicpc.net/problem/2133

N = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
dp[4] = 11


def sol(n):
    if n % 2 == 1:
        return 0
    else:
        if dp[n] == 0:
            tmp = n - 4
            result = 2
            result += sol(n-2) * 3
            while tmp >= 2:
                result += sol(tmp) * 2
                tmp -= 2
            dp[n] = result
        return dp[n]


print(sol(N))
