# https://www.acmicpc.net/problem/1822
import sys

input = sys.stdin.readline

# 파이썬 set이용한 풀이
# na, nb = map(int, input().split(' '))
# a_set = set(map(int, input().split(' ')))
# b_set = set(map(int, input().split(' ')))
# c_set = a_set - b_set
# if len(c_set) == 0:
#     print(0)
# else:
#     print(len(c_set))
#     print(' '.join(list(map(str, sorted(list(c_set))))))

# 이분탐색 풀이
na, nb = map(int, input().split(' '))
a_list = sorted(list(map(int, input().split(' '))))
b_list = sorted(list(map(int, input().split(' '))))


def search(s_num):
    left, right = 0, nb - 1
    while left <= right:
        mid = (left + right) // 2
        if b_list[mid] == s_num:
            return False, -1
        if b_list[mid] < s_num:
            left = mid + 1
        else:
            right = mid - 1
    return True, s_num


result = []
for a in a_list:
    result_bool, result_val = search(a)
    if result_bool:
        result.append(str(result_val))

if result:
    print(len(result))
    print(' '.join(result))
else:
    print(0)
