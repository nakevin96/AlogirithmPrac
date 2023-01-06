'''
토마토를 보관하는 큰 창고가 존재한다
N, M 격자 상자에 토마토를 보관하며
토마토 중 익지 않은 토마토들이 익은 토마토 영향을 받아 익는다
1은 익은 토마토 0은 익지 않은 토마토 -1은 토마토가 없는 칸이며
모두 익은 상태가 입력이면 0 모두 익지 못하는 상황이면 -1을 출력한다.
'''

# 토마토 상자를 탐색하며 1이 존재하면 BFS를 이용해 0을 1로 바꿔나간다

from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().rstrip().split(" "))
box_info = []
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()
for n_idx in range(n):
    box_info.append(list(map(int, stdin.readline().rstrip().split(" "))))
    for m_idx in range(m):
        if box_info[n_idx][m_idx] == 1:
            queue.append((n_idx, m_idx, 1))
        elif box_info[n_idx][m_idx] == -1:
            visited[n_idx][m_idx] = -1
dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]


while queue:
    curr_n, curr_m, curr_day = queue.popleft()
    if visited[curr_n][curr_m] == 0:
        visited[curr_n][curr_m] = curr_day
        for i in range(4):
            if curr_n + dn[i] < 0 or curr_m + dm[i] < 0 or curr_n + dn[i] >= n or curr_m + dm[i] >= m:
                continue
            if visited[curr_n+dn[i]][curr_m+dm[i]] == 0:
                queue.append((curr_n+dn[i], curr_m+dm[i], curr_day+1))

result = 0
is_wrong = False
for _n in range(n):
    for _m in range(m):
        if visited[_n][_m] == 0:
            is_wrong = True
            break
        result = max(result, visited[_n][_m])

    if is_wrong:
        print("-1")
        break
if not is_wrong:
    print(result-1)
