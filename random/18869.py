from sys import stdin
from collections import defaultdict

input = stdin.readline
result_dict = defaultdict(int)


def compress_planet(planet_list):
    sorted_planet = sorted(list(set(planet_list)))
    planet_dict = dict()
    for idx in range(len(sorted_planet)):
        planet_dict[sorted_planet[idx]] = str(idx)
    tmp = []
    for p in planet_list:
        tmp.append(planet_dict[p])
    return ','.join(tmp)


M, N = map(int, input().rstrip().split(' '))
for _ in range(M):
    result_dict[compress_planet(list(map(int, input().rstrip().split(' '))))] += 1


def get_combination_val(n, r):
    target = 1
    divider = 1
    for m in range(n - r + 1, n + 1):
        target *= m
    for m in range(2, r + 1):
        divider *= m
    return target // divider


result = 0
for pair_key, pair_num in result_dict.items():
    if pair_num > 1:
        result += get_combination_val(pair_num, 2)

print(result)
