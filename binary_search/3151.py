# # 합이 0 : https://www.acmicpc.net/problem/3151
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# N_list = list(map(int, input().split(' ')))
# N_list.sort()
#
# if N < 3:
#     print(0)
# else:
#     result = 0
#     for first_selected_idx in range(N):
#         for second_selected_idx in range(first_selected_idx+1, N):
#             target_val = N_list[first_selected_idx] + N_list[second_selected_idx]
#             left, right = second_selected_idx + 1, N - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if N_list[mid] >= -1 * target_val:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             val1 = right
#
#             left, right = second_selected_idx + 1, N - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if N_list[mid] > -1 * target_val:
#                     right = mid - 1
#                 elif N_list[mid] <= -1 * target_val:
#                     left = mid + 1
#             val2 = left
#             result += (val2 - val1 + 1)
#     print(result)

# 두번쨰 실패
# N = int(input())
# N_list = list(map(int, input().split(' ')))
# N_list.sort()
# two_sum = list()
# for i in range(N):
#     for j in range(i + 1, N):
#         two_sum.append((N_list[i] + N_list[j], i, j))
#
# result = set()
# for t_sum, t1, t2 in two_sum:
#     target = -1 * t_sum
#     left, right = 0, N - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if N_list[mid] == target:
#             if mid != t1 and mid != t2:
#                 result.add(tuple(sorted([t1, t2, mid])))
#             break
#         if N_list[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
# print(len(result))


N = int(input())
N_list = list(map(int, input().split(' ')))
N_list.sort()


def upper_bound(ust, ued, t):
    left, right = ust, ued
    while left < right:
        mid = (left + right) // 2
        if N_list[mid] <= t:
            left = mid + 1
        else:
            right = mid
    return left


def lower_bound(lst, led, t):
    left, right = lst, led
    while left < right:
        mid = (left + right) // 2
        if N_list[mid] >= t:
            right = mid
        else:
            left = mid + 1
    return right


total = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        ub = upper_bound(j + 1, N, -1 * (N_list[i] + N_list[j]))
        lb = lower_bound(j + 1, N, -1 * (N_list[i] + N_list[j]))
        total += (ub - lb)
print(total)
