'''
체스판 위에 나이트가 원하는 위치에 가기 위해 움직여야 하는 횟수
'''

from sys import stdin
from collections import deque


def solution():
    i = int(stdin.readline().rstrip())
    curr_pos_r, curr_pos_c = map(int, stdin.readline().rstrip().split(" "))
    target_pos_r, target_pos_c = map(int, stdin.readline().rstrip().split(" "))

    visited = [[-1 for _ in range(i)] for _ in range(i)]

    queue = deque([(curr_pos_r, curr_pos_c, 0)])

    while queue:
        curr_r, curr_c, curr_val = queue.popleft()
        if visited[curr_r][curr_c] != -1:
            continue
        if curr_r == target_pos_r and curr_c == target_pos_c:
            return curr_val
        visited[curr_r][curr_c] = curr_val
        for idx in range(8):
            nr = curr_r + dr[idx]
            nc = curr_c + dc[idx]
            if nr < 0 or nc < 0 or nr >= i or nc >= i:
                continue

            if visited[nr][nc] == -1:
                queue.append((nr, nc, curr_val + 1))


dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]
t = int(stdin.readline().rstrip())
for _ in range(t):
    print(solution())
