import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())

dp = [[-1 for _ in range(4)] for _ in range(2)] if n <= 3 else [[-1 for _ in range(n + 1)] for _ in range(2)]
dp[1][1], dp[1][2], dp[1][3] = 1, 0, 1
dp[0][1], dp[0][2], dp[0][3] = 0, 1, 0


def game(stones, turn):
    if dp[turn][stones] == -1:
        opponent = 1 if turn == 0 else 0
        prev1, prev3 = game(stones-1, opponent), game(stones-3, opponent)
        if prev1 == turn or prev3 == turn:
            dp[turn][stones] = turn
            dp[opponent][stones] = opponent
        else:
            dp[turn][stones] = opponent
            dp[opponent][stones] = turn
    return dp[turn][stones]


result = game(n, 1)
print('SK' if result == 1 else 'CY')
