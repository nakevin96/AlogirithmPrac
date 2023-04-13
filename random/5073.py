# https://www.acmicpc.net/problem/5073
import sys
from collections import Counter

input = sys.stdin.readline
while True:
    n_list = list(map(int, input().rstrip().split(' ')))
    n_list.sort()
    if n_list[0] == 0:
        break
    if n_list[0] + n_list[1] <= n_list[2]:
        print('Invalid')
    else:
        count_n_list = Counter(n_list)
        key_len = len(count_n_list)
        if key_len == 1:
            print('Equilateral')
        elif key_len == 2:
            print('Isosceles')
        elif key_len == 3:
            print('Scalene')
