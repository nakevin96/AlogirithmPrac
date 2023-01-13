'''
재난방재청에서 많은 비가 내리는 장마철에 대비해서 아래와 같은 일을 계획중이다
높이 정보를 파악하고 비가 내렸을 때 안정한 영역이 몇 개 인지 알아보자.
'''
from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
height_info = []
max_height = 0
result = 1

for _r in range(n):
    height_info.append(list(map(int, stdin.readline().rstrip().split(" "))))
    max_height = max(max_height, max(height_info[_r]))

for h in range(1, max_height):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    tmp_result = 0
    for _r in range(n):
        for _c in range(n):
            if height_info[_r][_c] - h > 0 and visited[_r][_c] == 0:
                tmp_result += 1
                queue = deque([(_r, _c)])
                while queue:
                    curr_r, curr_c = queue.popleft()
                    if visited[curr_r][curr_c] == 1:
                        continue
                    visited[curr_r][curr_c] = 1
                    for i in range(4):
                        nr = curr_r + dr[i]
                        nc = curr_c + dc[i]
                        if nr < 0 or nc < 0 or nr >= n or nc >= n:
                            continue
                        if height_info[nr][nc] - h > 0 and visited[nr][nc] == 0:
                            queue.append((nr, nc))
    result = max(result, tmp_result)

print(result)
