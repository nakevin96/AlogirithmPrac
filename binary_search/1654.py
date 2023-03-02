# 랜선 자르기
# https://www.acmicpc.net/problem/1654
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

len_list = []
K, N = map(int, input().rstrip().split(' '))
for _ in range(K):
    len_list.append(int(input().rstrip()))
len_list.sort()


def get_total_cable_num(unit_len):
    result = 0
    for l in len_list:
        result += (l // unit_len)
    return result


def search_max_len(left, right, cable_num):
    if left == right:
        return left
    curr_len = (left + right+1) // 2
    curr_cable_num = get_total_cable_num(curr_len)
    # 자른 갯수가 목표로 하는 갯수 보다 작을 경우 길이를 줄여야 함
    # 자른 갯수가 목표로 하는 갯수 보다 클 경우 길이를 늘려야 함
    # 자른 갯수가 목표로 하는 갯수와 같을 경우 역시 더 길게 자를 수 있는 가능성이 있으므로 길이를 늘려야함
    if curr_cable_num >= cable_num:
        return search_max_len(curr_len, right, cable_num)
    else:
        return search_max_len(left, curr_len-1, cable_num)


print(search_max_len(1, len_list[-1], N))
