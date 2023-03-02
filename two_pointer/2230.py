import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))
N_list = []
for _ in range(N):
    N_list.append(int(input()))
N_list.sort()

# 이분 탐색 풀이
# is_m = False
# result = N_list[-1] - N_list[0]
# for start_idx in range(N - 1):
#     left, right = start_idx, N - 1
#     mid = (left + right) // 2
#     while left < right:
#         mid = (left + right) // 2
#         if N_list[start_idx] + M == N_list[mid]:
#             is_m = True
#             break
#         if N_list[start_idx] + M > N_list[mid]:
#             left = mid+1
#         else:
#             right = mid
#     if is_m:
#         break
#     else:
#         tmp = N_list[left] - N_list[start_idx]
#         if tmp >= M:
#             result = min(result, tmp)
#
# if is_m:
#     print(M)
# else:
#     print(result)

# 투포인터 풀이
sp, ep = 0, 0
result = 2000000001
while True:
    if sp >= N-1 or ep >= N:
        break
    sub_val = N_list[ep] - N_list[sp]
    if sub_val == M:
        result = M
        break
    if sub_val < M:
        ep += 1
    else:
        if sub_val < result:
            result = sub_val
        sp += 1
print(result)
