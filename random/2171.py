# https://www.acmicpc.net/problem/2171
# 2차원 평면 위 N개의 점 존재 N[1:5_000]
# 이 점들 중 서로 다른 네개의 점을 잡아 연결하면 사각형
# 사각형들 중 X축과 Y축에 평행한 직사각형의 개수를 구해라

# 좌표 범위는 [-1_000_000_000 : 1_000_000_000]
from sys import stdin

input = stdin.readline

N = int(input())
pos_list = []
pos_set = set()
for _ in range(N):
    x, y = map(int, input().split(' '))
    pos_list.append((x, y))
    pos_set.add((x, y))

result = 0
for p1 in range(N):
    for p2 in range(p1 + 1, N):
        if (pos_list[p1][0] == pos_list[p2][0]) or (pos_list[p1][1] == pos_list[p2][1]):
            continue
        target_pos1 = (pos_list[p1][0], pos_list[p2][1])
        target_pos2 = (pos_list[p2][0], pos_list[p1][1])

        if (target_pos1 in pos_set) and (target_pos2 in pos_set):
            result += 1

print(result // 2)
