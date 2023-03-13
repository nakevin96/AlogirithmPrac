# 2xn 타일링 2 https://www.acmicpc.net/problem/11727
import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
dp = [0 for _ in range(1002)]
dp[1], dp[2] = 1, 3


def get_answer(block_len):
    if dp[block_len] == 0:
        tmp_val = get_answer(block_len - 1) + (2 * get_answer(block_len - 2))
        dp[block_len] = (tmp_val % 10007)
    return dp[block_len]


print(get_answer(n))


# 다른 풀이
# 2xn 타일링 2 https://www.acmicpc.net/problem/11727
#
# n = int(input())
# dp = [0 for _ in range(1002)]
# dp[1], dp[2] = 1, 3
# if n <= 2:
#     print(dp[n])
# else:
#     for curr_n in range(3, n + 1):
#         dp[curr_n] = (dp[curr_n - 1] + (2 * dp[curr_n - 2])) % 10007
#     print(dp[n])
