# 정수 삼각형 : https://www.acmicpc.net/problem/1932
import sys
input = sys.stdin.readline

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
for r in range(N):
    tmp = list(map(int, input().rstrip().split(' ')))
    for c in range(len(tmp)):
        graph[r][c] = tmp[c]

for r in range(1, N):
    for c in range(N):
        if c == 0:
            graph[r][c] += graph[r-1][c]
        else:
            graph[r][c] += max(graph[r-1][c], graph[r-1][c-1])

print(max(graph[-1]))


