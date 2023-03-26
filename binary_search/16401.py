# 과자 나눠주기: https://www.acmicpc.net/problem/16401
import math

M, N = map(int, input().split(' '))
N_list = list(map(int, input().split(' ')))
N_list.sort()


def find_n_list_idx(target):
    left, right = 0, N - 1
    tmp_result = N
    while left <= right:
        mid = (left + right) // 2
        if N_list[mid] >= target:
            tmp_result = min(mid, tmp_result)
            right = mid - 1
        else:
            left = mid + 1
    if tmp_result == N:
        return -1
    return tmp_result


def get_best_stick_len():
    min_len, max_len = 1, N_list[-1]
    result = 0
    while min_len <= max_len:
        mid_len = (min_len + max_len) // 2
        n_list_idx = find_n_list_idx(mid_len)
        total_stick_num = 0
        for i in range(n_list_idx, N):
            total_stick_num += (N_list[i] // mid_len)
        if total_stick_num >= M:
            result = max(result, mid_len)
            min_len = mid_len + 1
        else:
            max_len = mid_len - 1
    return result


print(get_best_stick_len())


def sol():
    def solve(x):
        if x == 0:
            return True
        cnt = 0
        for i in range(N):
            cnt += (N_list[i] // x)
        return cnt >= M

    st, en = 0, N_list[-1]
    while st < en:
        mid = (st + en + 1) // 2
        if solve(mid):
            st = mid
        else:
            en = mid - 1
    return st


print(sol())
