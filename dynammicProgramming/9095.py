import sys

input = sys.stdin.readline

stair_num = int(input())
dp = [0 for _ in range(stair_num + 1)]
stairs = [0]
for _ in range(stair_num):
    stairs.append(int(input()))
if stair_num <= 2:
    print(sum(stairs))
else:
    dp[1] = stairs[1]
    dp[2] = stairs[2]
    for si in range(3, stair_num + 1):
        dp[si] = min(dp[si - 2], dp[si - 3]) + stairs[si]

    print(sum(stairs) - min(dp[stair_num - 1], dp[stair_num - 2]))
