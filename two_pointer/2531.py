# 회전 초밥 : https://www.acmicpc.net/problem/2531
import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split(' '))
sushi_list = []
for _ in range(N):
    sushi_list.append(int(input()))

# 이전 풀이
# sushi_list.extend(sushi_list)
# eat_dict = dict()
# eat_dict[c] = 1
# for _k in range(k):
#     if sushi_list[_k] in eat_dict:
#         eat_dict[sushi_list[_k]] += 1
#     else:
#         eat_dict[sushi_list[_k]] = 1
#
# result = 0
# for n in range(N):
#     result = max(result, len(eat_dict))
#     next_sushi = n + k
#     pass_sushi = n
#     if sushi_list[next_sushi] in eat_dict:
#         eat_dict[sushi_list[next_sushi]] += 1
#     else:
#         eat_dict[sushi_list[next_sushi]] = 1
#     eat_dict[sushi_list[pass_sushi]] -= 1
#     if eat_dict[sushi_list[pass_sushi]] == 0:
#         del eat_dict[sushi_list[pass_sushi]]
#
# print(result)

# 2023 04 03 다시 풀어보기
sushi_list.extend(sushi_list[:k])
sushi_dict = dict()
result = 0
curr_result = 0

for i in range(k):
    if sushi_list[i] not in sushi_dict:
        sushi_dict[sushi_list[i]] = 1
        curr_result += 1
    else:
        sushi_dict[sushi_list[i]] += 1

result = curr_result

for i in range(N):
    if c not in sushi_dict:
        result = max(result, curr_result+1)
    else:
        result = max(result, curr_result)
    in_dish, out_dish = sushi_list[i + k], sushi_list[i]
    if in_dish not in sushi_dict:
        sushi_dict[in_dish] = 1
        curr_result += 1
    else:
        sushi_dict[in_dish] += 1

    sushi_dict[out_dish] -= 1
    if sushi_dict[out_dish] == 0:
        del sushi_dict[out_dish]
        curr_result -= 1

if c not in sushi_dict:
    result = max(result, curr_result+1)
else:
    result = max(result, curr_result)

print(result)
