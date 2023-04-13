# 연산자 끼워넣기: https://www.acmicpc.net/problem/14888
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
N_list = list(map(int, input().split(' ')))
O_list = list(map(int, input().split(' ')))
# o_list = []
# for i, o in enumerate(O_list):
#     o_list.extend([i] * o)

max_val = -1 * float('inf')
min_val = float('inf')


def dfs(select, result):
    global max_val, min_val
    if select == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    for idx in range(len(O_list)):
        if O_list[idx] > 0:
            tmp_result = result
            O_list[idx] -= 1
            next_val = N_list[select]
            if idx == 0:
                tmp_result += next_val
            elif idx == 1:
                tmp_result -= next_val
            elif idx == 2:
                tmp_result *= next_val
            else:
                if next_val == 0:
                    return
                if tmp_result < 0:
                    tmp_result *= -1
                    tmp_result //= next_val
                    tmp_result *= -1
                else:
                    tmp_result //= next_val
            dfs(select + 1, tmp_result)
            O_list[idx] += 1


dfs(1, N_list[0])
print(max_val)
print(min_val)

# o_list = []
# for i, o in enumerate(O_list):
#     o_list.extend([i] * o)
#
# max_val = -1 * float('inf')
# min_val = float('inf')
# candidates = list(permutations(o_list, len(o_list)))
# for candidate in candidates:
#     tmp_result = N_list[0]
#     for i in range(len(o_list)):
#         operator = candidate[i]
#         next_num = N_list[i+1]
#         if operator == 0:
#             tmp_result += next_num
#         elif operator == 1:
#             tmp_result -= next_num
#         elif operator == 2:
#             tmp_result *= next_num
#         elif operator == 3:
#             if tmp_result >= 0:
#                 tmp_result = tmp_result // next_num
#             else:
#                 tmp_result *= -1
#                 tmp_result = tmp_result // next_num
#                 tmp_result *= -1
#         else:
#             print('error')
#     max_val = max(tmp_result, max_val)
#     min_val = min(tmp_result, min_val)
#
# print(max_val)
# print(min_val)
