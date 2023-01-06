'''
mxn 크기의 모눈종이가 있다
이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때
이들 K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다
'''

from sys import stdin
from collections import deque


def solution():
    result = []
    c, r, k = map(int, stdin.readline().rstrip().split(" "))
    visited = [[0 for _c in range(c)] for _r in range(r)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for _k in range(k):
        r1, c1, r2, c2 = map(int, stdin.readline().rstrip().split(" "))
        for _r in range(r1, r2):
            for _c in range(c1, c2):
                visited[_r][_c] = 1

    for _r in range(r):
        for _c in range(c):
            if visited[_r][_c] == 0:
                tmp_result = 0
                queue = deque([(_r, _c)])
                while queue:
                    curr_r, curr_c = queue.popleft()
                    if visited[curr_r][curr_c] != 0:
                        continue
                    tmp_result += 1
                    visited[curr_r][curr_c] = 1
                    for i in range(4):
                        nr = curr_r + dr[i]
                        nc = curr_c + dc[i]
                        if nr < 0 or nc < 0 or nr >= r or nc >= c:
                            continue
                        if visited[nr][nc] == 0:
                            queue.append((nr, nc))
                result.append(tmp_result)

    print(len(result))
    print(" ".join(map(str, sorted(result))))


solution()
