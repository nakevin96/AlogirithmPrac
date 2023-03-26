# https://www.acmicpc.net/problem/2302
import sys

input = sys.stdin.readline

dp = [0 for _ in range(50)]
dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
for i in range(4, 50):
    dp[i] = dp[i - 1] + dp[i - 2]

N = int(input())
M = int(input())

if M == 0:
    print(dp[N])
else:
    curr_seat = 0
    result = []

    for _ in range(M):
        fixed = int(input())
        if fixed-curr_seat-1 > 0:
            result.append(fixed - curr_seat - 1)
        curr_seat = fixed
    if curr_seat < N:
        result.append(N - curr_seat)
    if result:
        result_mul = 1
        for r in result:
            result_mul *= dp[r]
        print(result_mul)
    else:
        print(1)
