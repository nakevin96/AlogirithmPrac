# 가운데를 말해요: https://www.acmicpc.net/problem/1655
import sys
import heapq

input = sys.stdin.readline
N = int(input())
max_heap = []
min_heap = []
for _ in range(N):
    num = int(input())
    if len(max_heap) <= len(min_heap):
        heapq.heappush(max_heap, -1 * num)
    else:
        heapq.heappush(min_heap, num)
    if min_heap and (min_heap[0] < -1 * max_heap[0]):
        heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))
        heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))
    print(-1 * max_heap[0])
