# 돌멩이 제거: https://www.acmicpc.net/problem/1867
import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().rstrip().split(' '))
r_dict = defaultdict(int)
c_dict = defaultdict(int)
stone_check = [[False for _ in range(n)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().rstrip().split(' '))
    r, c = r-1, c-1
    r_dict[r] += 1
    c_dict[c] += 1
    stone_check[r][c] = True

candidate_list =




