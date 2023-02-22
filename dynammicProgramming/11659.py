import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split(" "))
num_list = list(map(int, input().split(" ")))
dp = [0 for _ in range(100000)]
dp[0] = num_list[0]


def get_sum(n):
    if dp[n] > 0:
        return dp[n]
    else:
        tmp = get_sum(n - 1) + num_list[n]
        dp[n] = tmp
        return dp[n]


for _ in range(M):
    i, j = map(int, input().split(" "))
    zero2i = get_sum(i - 1)
    zero2j = get_sum(j - 1)
    print(zero2j - zero2i + num_list[i - 1])
