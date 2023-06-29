# from sys import stdin
# from itertools import combinations
# from collections import defaultdict
#
# input = stdin.readline
#
# T = int(input())
# n = int(input())
# a_list = [0]
# a_list.extend(list(map(int, input().split(' '))))
# a_sum_list = [0]
# for a_idx in range(1, n + 1):
#     a_sum_list.append(a_sum_list[-1] + a_list[a_idx])
#
# check_dict = defaultdict(int)
# for a1, a2 in combinations(a_sum_list, 2):
#     check_dict[T - (a2 - a1)] += 1
#
# m = int(input())
# b_list = [0]
# b_list.extend(list(map(int, input().split(' '))))
# b_sum_list = [0]
# for b_idx in range(1, m + 1):
#     b_sum_list.append(b_sum_list[-1] + b_list[b_idx])
#
# result = 0
# for b1, b2 in combinations(b_sum_list, 2):
#     if (b2 - b1) in check_dict:
#         result += check_dict[b2-b1]
# print(result)
from sys import stdin
from itertools import combinations
from collections import defaultdict

input = stdin.readline


def get_sum_list(num_list):
    result_sum_list = [0]
    for num_idx in range(1, len(num_list)):
        result_sum_list.append(result_sum_list[-1] + num_list[num_idx])
    return result_sum_list


T = int(input())
n = int(input())
a_list = [0]
a_list.extend(list(map(int, input().split(' '))))

a_sum_list = get_sum_list(a_list)

check_dict = defaultdict(int)
for a1, a2 in combinations(a_sum_list, 2):
    check_dict[T - (a2 - a1)] += 1

m = int(input())
b_list = [0]
b_list.extend(list(map(int, input().split(' '))))
b_sum_list = get_sum_list(b_list)

result = 0
for b1, b2 in combinations(b_sum_list, 2):
    if (b2 - b1) in check_dict:
        result += check_dict[b2 - b1]
print(result)
