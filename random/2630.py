# 색종이 만들기: https://www.acmicpc.net/problem/2630
from sys import stdin

input = stdin.readline

N = int(input())
map_info = []
for _ in range(N):
    map_info.append(input().rstrip().split(' '))

zero_count = 0
one_count = 0


def is_united(square_size, start_r, start_c):
    global zero_count, one_count
    if square_size == 1:
        if map_info[start_r][start_c] == '0':
            zero_count += 1
        else:
            one_count += 1
        return

    is_done = True
    base = map_info[start_r][start_c]
    for r in range(start_r, start_r + square_size):
        for c in range(start_c, start_c + square_size):
            if map_info[r][c] != base:
                is_done = False
                break
        if not is_done:
            break
    if is_done:
        if base == '0':
            zero_count += 1
        else:
            one_count += 1
        return

    is_united(square_size // 2, start_r, start_c)
    is_united(square_size // 2, start_r + (square_size // 2), start_c)
    is_united(square_size // 2, start_r, start_c + (square_size // 2))
    is_united(square_size // 2, start_r + (square_size // 2), start_c + (square_size // 2))


is_united(N, 0, 0)
print(zero_count)
print(one_count)
