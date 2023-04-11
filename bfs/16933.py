from sys import stdin
from collections import deque

input = stdin.readline

N, M, K = map(int, input().rstrip().split(' '))
map_info = []
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(N):
    map_info.append(list(input().rstrip()))
visited = [[[False for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True
# curr row, curr column, curr num of broken wall, curr move distance
queue = deque([(0, 0, 0, 1)])


def bfs():
    day = True
    while queue:
        q_len = len(queue)
        for _ in range(q_len):
            cr, cc, cb, cd = queue.popleft()
            if cr == N - 1 and cc == M - 1:
                return cd
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue
                if map_info[nr][nc] == '0':
                    if not visited[nr][nc][cb]:
                        visited[nr][nc][cb] = True
                        queue.append((nr, nc, cb, cd + 1))
                else:
                    if day:
                        if cb + 1 <= K and not visited[nr][nc][cb + 1]:
                            visited[nr][nc][cb + 1] = True
                            queue.append((nr, nc, cb + 1, cd + 1))
                    else:
                        if cb + 1 <= K and not visited[nr][nc][cb + 1]:
                            queue.append((cr, cc, cb, cd + 1))
        day = not day
    return -1


print(bfs())
