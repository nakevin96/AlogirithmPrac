# # 숫자카드 2
# import sys
#
# sys.setrecursionlimit(10 ** 6)
# N = int(input())
# N_tmp_list = list(map(int, input().split(' ')))
# M = int(input())
# M_list = list(map(int, input().split(' ')))
# N_list = []
# N_dict = dict()
# for n in N_tmp_list:
#     if n not in N_dict:
#         N_dict[n] = 1
#         N_list.append(n)
#     else:
#         N_dict[n] += 1
#
# # dict 안쓰고 binary search로 구현해봄
# # N_list.sort()
# #
# #
# # def binary_search(left, right, val):
# #     if left > right:
# #         return 0
# #     mid = (left + right) // 2
# #     if N_list[mid] == val:
# #         return N_dict[val]
# #
# #     if val < N_list[mid]:
# #         return binary_search(left, mid - 1, val)
# #     else:
# #         return binary_search(mid + 1, right, val)
# #
# #
# # result = []
# # for m in M_list:
# #     result.append(str(binary_search(0, len(N_list) - 1, m)))
# # print(f' '.join(result))
#
# result = []
# for m in M_list:
#     result.append('0' if m not in N_dict else str(N_dict[m]))
# print(f' '.join(result))

import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
N_list = list(map(int, input().split(' ')))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split(' ')))


def find_left(left, right, val):
    if left == right:
        return left
    mid = (left + right) // 2
    # 찾으려는 값이 중앙 값보다 작거나 같은 경우 왼쪽 영역 지정
    if N_list[mid] >= val:
        return find_left(left, mid, val)
    else:
        return find_left(mid + 1, right, val)


def find_right(left, right, val):
    if left == right:
        return left
    mid = (left + right) // 2
    # 찾으려는 값이 중앙 값보다  크거나 같으면 우측 영역 지정
    if N_list[mid] <= val:
        return find_right(mid + 1, right, val)
    else:
        return find_right(left, mid, val)


result = []
for m in M_list:
    r_pos = find_right(0, N, m)
    l_pos = find_left(0, N, m)
    result.append(str(r_pos - l_pos))
print(' '.join(result))
