# 숫자 카드 : https://www.acmicpc.net/problem/10815
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split(' ')))
M = int(input())
M_list = list(map(int, input().split(' ')))

N_list.sort()

result = []


def search(s_num):
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if N_list[mid] == s_num:
            return '1'
        if N_list[mid] < s_num:
            left = mid + 1
        else:
            right = mid - 1
    return '0'


for m in M_list:
    result.append(search(m))

print(' '.join(result))
