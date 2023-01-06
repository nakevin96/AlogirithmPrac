'''
N*M 미로 존재 1은 이동가능 0은 이동 불가
(1, 1)에서 출발하여 (N,M)의 위치로 이동할 때 지나야 하는 최소 칸수
'''
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split(" "))
if n == 1 and m == 1:
    print("1")
else:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    map_info = []
    for _ in range(n):
        map_info.append(list(map(int, list(stdin.readline().rstrip()))))
    queue = deque([(0, 0, 1)])
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]

    while queue:
        curr_n, curr_m, curr_val = queue.popleft()
        if curr_n == n - 1 and curr_m == m - 1:
            print(curr_val)
            break
        if visited[curr_n][curr_m] == 1:
            continue
        map_info[curr_n][curr_m] = curr_val
        visited[curr_n][curr_m] = 1
        for i in range(4):
            if curr_n + dn[i] < 0 or curr_n + dn[i] >= n or curr_m + dm[i] < 0 or curr_m + dm[i] >= m:
                continue
            if map_info[curr_n + dn[i]][curr_m + dm[i]] == 0 or visited[curr_n+dn[i]][curr_m+dm[i]] == 1:
                continue
            queue.append((curr_n + dn[i], curr_m + dm[i], curr_val + 1))
