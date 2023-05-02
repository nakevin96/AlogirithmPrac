# 숨바꼭질 3: https://www.acmicpc.net/problem/13549
import heapq

N, K = map(int, input().split(' '))
visited = [-1 for _ in range(200005)]
queue = [(0, N)]
while queue:
    curr_time, curr_pos = heapq.heappop(queue)
    if curr_pos == K:
        print(curr_time)
        break
    if visited[curr_pos] != -1 and visited[curr_pos] <= curr_time:
        continue
    visited[curr_pos] = curr_time
    if curr_pos - 1 >= 0:
        heapq.heappush(queue, (curr_time + 1, curr_pos - 1))
    if curr_pos + 1 <= 100000:
        heapq.heappush(queue, (curr_time + 1, curr_pos + 1))
    if curr_pos * 2 <= 100000:
        heapq.heappush(queue, (curr_time, curr_pos * 2))
