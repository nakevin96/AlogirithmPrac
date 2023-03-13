# 가장 큰 정사각형: https://www.acmicpc.net/problem/1915
n, m = map(int, input().split(' '))
map_info = []
for _ in range(n):
    map_info.append(list(map(int, list(input()))))
# dp = [[0 for _ in range(m)] for _ in range(n)]
#
# result = 0
# for r in range(n):
#     for c in range(m):
#         if map_info[r][c] == 1:
#             dr, dc = r-1, c-1
#             if dr < 0 or dc < 0:
#                 dp[r][c] = 1
#             elif dp[dr][dc] > 0:
#                 check = dp[dr][dc]
#                 for ri in range(1, check+1):
#                     if dp[r-ri][c] == 0:
#                         check = ri-1
#                         break
#                 for ci in range(1, check+1):
#                     if dp[r][c-ci] == 0:
#                         check = ci-1
#                         break
#                 dp[r][c] = 1 + check
#             else:
#                 dp[r][c] = 1
#             result = max(result, dp[r][c])

# 다른 풀이
# 위 왼 오 중 가장 작은거에 +1하면 되는 거였음.
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

result = 0
for r in range(n):
    for c in range(m):
        if map_info[r][c] == 1:
            dp[r + 1][c + 1] = min(dp[r][c + 1], dp[r + 1][c], dp[r][c]) + 1
            result = max(result, dp[r + 1][c + 1])

print(result * result)
