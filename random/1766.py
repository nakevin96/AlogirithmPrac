import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split(' '))

connect_info = [[] for _ in range(N + 1)]
inbound_count = [0 for _ in range(N + 1)]
inbound_count[0] = -1
for _ in range(M):
    A, B = map(int, input().split(' '))
    connect_info[A].append(B)
    inbound_count[B] += 1

result = []
queue = [idx for idx, c in enumerate(inbound_count) if c == 0]
heapq.heapify(queue)

while queue:
    curr_prob = heapq.heappop(queue)
    result.append(curr_prob)

    for next_prob in connect_info[curr_prob]:
        inbound_count[next_prob] -= 1
        if inbound_count[next_prob] == 0:
            heapq.heappush(queue, next_prob)
print(*result)
