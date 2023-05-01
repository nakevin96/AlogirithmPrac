# 최단 경로 : https://www.acmicpc.net/problem/1753
# 다익스트라는 간선의 코스트가 음수면 안된다
# 다익스트라는 한 점에서 다른 점까지 이동 시 최단 거리를 구하는 알고리즘이다.
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split(' '))
K = int(input())
INF = float('inf')
check_list = [INF for _ in range(V)]
map_info = [[] for _ in range(V)]
for _ in range(E):
    v1, v2, cost = map(int, input().split(' '))
    map_info[v1 - 1].append([v2 - 1, cost])

queue = [(0, K - 1)]
while queue:
    curr_cost, curr_v = heapq.heappop(queue)
    if check_list[curr_v] > curr_cost:
        check_list[curr_v] = curr_cost
    else:
        continue
    for next_v, next_cost in map_info[curr_v]:
        heapq.heappush(queue, (curr_cost + next_cost, next_v))

for i in range(V):
    if i == K - 1:
        print(0)
    elif check_list[i] == INF:
        print('INF')
    else:
        print(check_list[i])
