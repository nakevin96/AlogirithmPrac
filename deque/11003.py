# from sys import stdin
# from collections import deque
#
# n, m = map(int, stdin.readline().rstrip().split(" "))
# dq = deque()
# num_list = list(map(int, stdin.readline().rstrip().split(" ")))
# result = []
#
# for i in range(n):
#     while dq and dq[-1][1] >= num_list[i]:
#         dq.pop()
#
#     dq.append([i, num_list[i]])
#
#     while dq and dq[0][0] <= i - m:
#         dq.popleft()
#     print(dq[0][1], end=' ')

from sys import stdin
import heapq

n, m = map(int, stdin.readline().rstrip().split(" "))
n_list = list(map(int, stdin.readline().rstrip().split(" ")))
pq = []

for i in range(n):
    heapq.heappush(pq, (n_list[i], i))
    while pq[0][1] < max(0, i-m+1):
        heapq.heappop(pq)
    print(pq[0][0], end=' ')
