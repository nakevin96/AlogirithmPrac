# 수 찾기
import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())
N_list = list(map(int, input().split(' ')))
M = int(input())
M_list = list(map(int, input().split(' ')))

N_list.sort()


def binary_search(left, right, val):
    if left >= right:
        if N_list[left] == val:
            return 1
        else:
            return 0
    mid = (left + right) // 2
    if N_list[mid] == val:
        return 1

    if val < N_list[mid]:
        return binary_search(left, mid, val)
    else:
        return binary_search(mid + 1, right, val)


for m in M_list:
    print(binary_search(0, N - 1, m))
