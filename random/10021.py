# Watering the Fields : https://www.acmicpc.net/problem/10021
from sys import stdin
from itertools import combinations

input = stdin.readline

N, C = map(int, input().rstrip().split(' '))
dot_info = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
candidates = list(combinations(dot_info, 2))


def get_dist(pos_l):
    return (((pos_l[0][0] - pos_l[1][0]) ** 2) + ((pos_l[0][1] - pos_l[1][1]) ** 2), pos_l[0], pos_l[1])


candidates = [(dist, pos1, pos2) for dist, pos1, pos2 in map(get_dist, candidates) if dist >= C]
candidates.sort(key=lambda x: x[0])
print(candidates)
