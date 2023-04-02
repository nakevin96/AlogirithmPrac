# 세 용액: https://www.acmicpc.net/problem/2473
N = int(input())
N_list = list(map(int, input().split(' ')))
N_list.sort()
result = float('inf')
result_list = []

# 이분 탐색 풀이
# is_find = False
# for i in range(N-1):
#     if is_find:
#         break
#     for j in range(i+1, N):
#         two_sum = N_list[i] + N_list[j]
#         target = -1 * two_sum
#         st, en = j+1, N
#         while st < en:
#             mid = (st + en) // 2
#             if N_list[mid] >= target:
#                 en = mid
#             else:
#                 st = mid + 1
#         for c in range(st-2, st+3):
#             if j+1 <= c <= N-1:
#                 tmp_result = two_sum + N_list[c]
#                 if tmp_result == 0:
#                     is_find = True
#                     result = 0
#                     result_str = [str(N_list[i]), str(N_list[j]), str(N_list[c])]
#                     break
#                 if abs(tmp_result) < result:
#                     result = abs(tmp_result)
#                     result_str = [str(N_list[i]), str(N_list[j]), str(N_list[c])]
#         if is_find:
#             break
#
# print(' '.join(result_str))

# 투포인터 풀이
is_find = False
for l1 in range(N - 2):
    if is_find:
        break
    l2, l3 = l1 + 1, N - 1
    while l2 < l3:
        curr_sum = N_list[l1] + N_list[l2] + N_list[l3]
        if abs(curr_sum) < result:
            result = abs(curr_sum)
            result_list = [N_list[l1], N_list[l2], N_list[l3]]
        if curr_sum < 0:
            l2 += 1
        elif curr_sum > 0:
            l3 -= 1
        else:
            is_find = True
        if is_find:
            break
print(*result_list)
