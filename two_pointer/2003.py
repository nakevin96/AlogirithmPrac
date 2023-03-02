N, M = map(int, input().split(' '))
N_list = list(map(int, input().split(' ')))

# 투포인터 풀이
# result = 0
# en = 0
# sum_val = N_list[0]
# for sn in range(N):
#     while en < N and sum_val < M:
#         en += 1
#         if en == N:
#             break
#         sum_val += N_list[en]
#     if en == N:
#         break
#     if sum_val == M:
#         result += 1
#     sum_val -= N_list[sn]
# print(result)

# 이분탐색 풀이
# 처음부터 끝까지
result = 0
for check_idx in range(N):
    left = check_idx
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        curr_sum = sum(N_list[check_idx:mid+1])
        if curr_sum == M:
            result += 1
            break
        elif curr_sum < M:
            left = mid + 1
        else:
            right = mid - 1
print(result)

