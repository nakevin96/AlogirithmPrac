'''
NxN 행렬로 표현이 가능한 종이가 있다.
-1, 0, 1 중 하나가 저장되어 있다
'''
from sys import stdin

N = int(stdin.readline().rstrip())
result = [0, 0, 0]
info = []
for _ in range(N):
    info.append(list(map(int, stdin.readline().rstrip().split(" "))))


def find_piece(n, r, c):
    if n == 1:
        result[info[r][c] + 1] += 1
        return

    base = info[r][c]
    is_done = True
    for _r in range(n):
        for _c in range(n):
            if info[r + _r][c + _c] != base:
                is_done = False
                break
    if is_done:
        result[base + 1] += 1
        return
    else:
        next_n = n // 3
        for nr in range(3):
            for nc in range(3):
                find_piece(next_n, r + (nr * next_n), c + (nc * next_n))


find_piece(N, 0, 0)
print(result[0])
print(result[1])
print(result[2])
