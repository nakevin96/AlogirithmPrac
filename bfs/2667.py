'''
단지 번호 붙이기
정사각형 모양의 지도가 존재한다
1은 집이 있는 곳을 0은 집이 없는 곳을 나타낸다
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고 단지에 번호를 붙이려한다.
단지수와 단지에 속한 집 수를 출력해라
'''
from sys import stdin
from collections import deque


def solution():
    n = int(stdin.readline().rstrip())
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    info = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        info.append(list(map(int, list(stdin.readline().rstrip()))))

    results = []
    for _r in range(n):
        for _c in range(n):
            if info[_r][_c] == 1 and visited[_r][_c] == 0:
                count = 0
                queue = deque([(_r, _c)])
                while queue:
                    curr_r, curr_c = queue.popleft()
                    if visited[curr_r][curr_c] == 1:
                        continue
                    visited[curr_r][curr_c] = 1
                    count += 1
                    for i in range(4):
                        nr = curr_r + dr[i]
                        nc = curr_c + dc[i]
                        if nr < 0 or nc < 0 or nr >= n or nc >= n:
                            continue
                        if info[nr][nc] == 1 and visited[nr][nc] == 0:
                            queue.append((nr, nc))
                results.append(count)
    print(len(results))
    for result in sorted(results):
        print(result)


solution()
