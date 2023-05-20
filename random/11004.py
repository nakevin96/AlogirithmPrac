# K번째 수 https://www.acmicpc.net/problem/11004

# def quick_select(target_idx, start_idx, end_idx):
#     pivot_idx = end_idx
#     left, right = start_idx, pivot_idx - 1
#     is_done = False
#
#     while not is_done:
#         while left <= right and N_list[left] <= N_list[pivot_idx]:
#             left += 1
#         while left <= right and N_list[pivot_idx] <= N_list[right]:
#             right -= 1
#
#         if right < left:
#             is_done = True
#         else:
#             N_list[left], N_list[right] = N_list[right], N_list[left]
#     N_list[pivot_idx], N_list[left] = N_list[left], N_list[pivot_idx]
#     result_idx = left
#     if result_idx == target_idx:
#         return N_list[result_idx]
#     elif result_idx < target_idx:
#         return quick_select(target_idx, result_idx + 1, end_idx)
#     else:
#         return quick_select(target_idx, start_idx, result_idx - 1)
import random
import sys
input = sys.stdin.readline


def quick_select(target_idx, start_idx, end_idx):
    while True:
        if start_idx == end_idx:
            return N_list[start_idx]

        pivot_idx = random.randint(start_idx, end_idx)
        N_list[pivot_idx], N_list[end_idx] = N_list[end_idx], N_list[pivot_idx]

        left, right = start_idx, end_idx - 1
        while left <= right:
            while left <= right and N_list[left] <= N_list[end_idx]:
                left += 1
            while left <= right and N_list[right] >= N_list[end_idx]:
                right -= 1
            if right < left:
                break
            N_list[left], N_list[right] = N_list[right], N_list[left]
        N_list[left], N_list[end_idx] = N_list[end_idx], N_list[left]

        if left == target_idx:
            return N_list[left]
        elif left < target_idx:
            start_idx = left + 1
        else:
            end_idx = left - 1


N, M = map(int, input().split(' '))
N_list = list(map(int, input().split(' ')))
print(quick_select(M - 1, 0, len(N_list) - 1))
