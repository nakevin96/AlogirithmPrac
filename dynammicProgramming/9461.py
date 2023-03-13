# 파도반 수열 : https://www.acmicpc.net/problem/9461
import sys

input = sys.stdin.readline
p_list = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
p_list.extend([-1 for _ in range(100)])
T = int(input())


def get_sol(c_num):
    if p_list[c_num] == -1:
        tmp = get_sol(c_num - 5) + get_sol(c_num - 1)
        p_list[c_num] = tmp
    return p_list[c_num]


for _ in range(T):
    print(get_sol(int(input())))
