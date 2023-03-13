# 회전 초밥 : https://www.acmicpc.net/problem/2531
import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split(' '))
sushi_list = []
for _ in range(N):
    sushi_list.append(int(input()))

sushi_list.extend(sushi_list)
eat_dict = dict()
eat_dict[c] = 1
for _k in range(k):
    if sushi_list[_k] in eat_dict:
        eat_dict[sushi_list[_k]] += 1
    else:
        eat_dict[sushi_list[_k]] = 1

result = 0
for n in range(N):
    result = max(result, len(eat_dict))
    next_sushi = n + k
    pass_sushi = n
    if sushi_list[next_sushi] in eat_dict:
        eat_dict[sushi_list[next_sushi]] += 1
    else:
        eat_dict[sushi_list[next_sushi]] = 1
    eat_dict[sushi_list[pass_sushi]] -= 1
    if eat_dict[sushi_list[pass_sushi]] == 0:
        del eat_dict[sushi_list[pass_sushi]]

print(result)