import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

dp = [[-1, -1] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]


def get_val(n):
    if n == 0 or n == 1:
        return dp[n]
    if dp[n][0] == -1:
        val1 = dp[n - 2] if dp[n - 2][0] != -1 else get_val(n - 2)
        val2 = dp[n - 1] if dp[n - 1][0] != -1 else get_val(n - 1)
        dp[n] = [val1[0] + val2[0], val1[1] + val2[1]]
    return dp[n]


for _ in range(T):
    val = get_val(int(input()))
    print(f'{val[0]} {val[1]}')
