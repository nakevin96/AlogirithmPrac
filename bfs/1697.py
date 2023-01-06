'''
수빈이는 동생과 숨바꼭질 중이다
수빈이는 N에 있고 동생은 K에 있다
수빈이는 걷거나 순간이동이 가능하며 걸었을 때는 +-1 순간이동시에는 2*X의 위치로 이동한다
수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하라
'''

from sys import stdin
from collections import deque

visited = [0 for _ in range(100001)]
n, k = map(int, stdin.readline().rstrip().split(" "))

queue = deque([(n, 0)])
while queue:
    pos, time = queue.popleft()
    visited[pos] = time
    if pos == k:
        print(time)
        break

    if pos + 1 <= 100000 and visited[pos+1] == 0:
        queue.append((pos+1, time+1))
    if pos - 1 >= 0 and visited[pos-1] == 0:
        queue.append((pos-1, time+1))
    if pos * 2 <= 100000 and visited[pos*2] == 0:
        queue.append((pos*2, time+1))

