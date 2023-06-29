# N, M = map(int, input().split(' '))
# app_memory = [0]
# app_memory.extend(list(map(int, input().split(' '))))
# MAX = sum(app_memory) + 1
# app_cost = [0]
# app_cost.extend(list(map(int, input().split(' '))))
#
# # 메모리 초과 발생
# # # dp[i][j] : i개의 앱이 존재할 때 j만큼의 메모리를 확보하는데 드는 최소 코스트
# # dp = [[MAX for _ in range(M + 1)] for _ in range(N + 1)]
# dp = [MAX for _ in range(M+1)]
#
# for app_idx in range(1, N + 1):
#     new_dp = [MAX for _ in range(M + 1)]
#     for target in range(M + 1):
#         # 크면 코스트 확보 가능
#         if app_memory[app_idx] >= target:
#             new_dp[target] = min(dp[target], app_cost[app_idx])
#         else:
#             # 더 작으면 해당 메모리 확보 불가
#             new_dp[target] = min(dp[target], dp[target - app_memory[app_idx]] + app_cost[app_idx])
#     dp = new_dp
#
# print(dp[M])

# from sys import stdin
#
# input = stdin.readline
#
# N, M = map(int, input().split(' '))
# app_memory = [0]
# app_memory.extend(list(map(int, input().split(' '))))
# app_cost = [0]
# app_cost.extend(list(map(int, input().split(' '))))
# MAX_COST = sum(app_cost)
# dp = [0 for _ in range(MAX_COST+1)]
#
# for app_idx in range(1, N+1):
#     for cost in range(MAX_COST, 0, -1):
#         if cost >= app_cost[app_idx]:
#             dp[cost] = max(dp[cost], dp[cost - app_cost[app_idx]] + app_memory[app_idx])
#
# result = 0
# while dp[result] < M:
#     result += 1
# print(result)

from sys import stdin

input = stdin.readline

N, M = map(int, input().split(' '))
app_memory = [0]
app_memory.extend(list(map(int, input().split(' '))))
app_cost = [0]
app_cost.extend(list(map(int, input().split(' '))))
MAX_COST = sum(app_cost)
dp = [0 for _ in range(MAX_COST + 1)]

for app_idx in range(1, N + 1):
    new_dp = [*dp]
    for cost in range(1, MAX_COST+1):
        if cost >= app_cost[app_idx]:
            new_dp[cost] = max(dp[cost], dp[cost - app_cost[app_idx]] + app_memory[app_idx])
    dp = new_dp
result = 0
while dp[result] < M:
    result += 1
print(result)
