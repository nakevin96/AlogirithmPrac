# 제곱수의 합 : https://www.acmicpc.net/problem/1699
import sys
sys.setrecursionlimit(10**6)
n = int(input())
dp = [-1 for _ in range(n + 1)]
dp[0], dp[1], dp[2], dp[3], dp[4] = 0, 1, 2, 3, 1


def get_val(num):
    if dp[num] == -1:
        s_num = int(num ** 0.5)
        if s_num ** 2 == num:
            dp[num] = 1
        else:
            min_val = n + 1
            for i in range(1, s_num + 1):
                min_val = min(min_val, get_val(num - (i ** 2)) + 1)
            dp[num] = min_val

    return dp[num]


print(get_val(n))
