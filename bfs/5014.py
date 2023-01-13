'''
F층으로 이루어진 고층 건물에 사무실이 있고 목적지는 G층이다
강호는 S층에 위치하고 있다
U버튼과 D버튼이 존재하는데 U는 U만큼만 D는 D만큼만 이동할 수 있다
'''
from sys import stdin
from collections import deque

f, s, g, u, d = map(int, stdin.readline().rstrip().split(" "))

queue = deque([(s, 0)])
visited = [0 for _ in range(f+1)]
visited[0] = 1
is_find = False

while queue:
    curr, val = queue.popleft()
    if visited[curr] != 0:
        continue
    if curr == g:
        is_find = True
        print(val)
        break
    visited[curr] = val
    if curr+u <= f and visited[curr+u] == 0:
        queue.append((curr+u, val+1))
    if curr-d > 0 and visited[curr-d] == 0:
        queue.append((curr-d, val+1))

if not is_find:
    print("use the stairs")
