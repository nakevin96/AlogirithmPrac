import sys
import heapq

input = sys.stdin.readline

queue = []
N = int(input())
for _ in range(N):
    heapq.heappush(queue, int(input()))

result = 0
while len(queue) > 1:
    pack1 = heapq.heappop(queue)
    pack2 = heapq.heappop(queue)
    result += pack1 + pack2
    heapq.heappush(queue, pack1 + pack2)
print(result)
