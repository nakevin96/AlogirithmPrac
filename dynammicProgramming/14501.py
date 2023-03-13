# 퇴사 : https://www.acmicpc.net/problem/14501

N = int(input())
N_list = [[0, 0]]
for _ in range(N):
    N_list.append(list(map(int, input().split(' '))))

# limit = [0 for _ in range(N + 1)]
# price = [0 for _ in range(N + 1)]
# limit[1], price[1] = N_list[1][0] + 1, N_list[1][1]
# for day in range(2, N + 1):
#     price[day] = N_list[day][1]
#     limit[day] = N_list[day][0] + day
#     for prev_day in range(1, day):
#         if limit[prev_day] <= day:
#             price[day] = max(price[day], price[prev_day] + N_list[day][1])
#
# result = 0
# for day in range(1, N+1):
#     if limit[day] <= N+1:
#         result = max(result, price[day])
# print(result)

# 다른 사람 풀이
dp = [0 for _ in range(20)]
for day in range(N, 0, -1):
    if N_list[day][0] + day <= N + 1:
        dp[day] = max(dp[day + N_list[day][0]] + N_list[day][1], dp[day + 1])
    else:
        dp[day] = dp[day + 1]
print(max(dp))
