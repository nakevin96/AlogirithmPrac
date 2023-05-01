# 최소비용구하기 2: https://www.acmicpc.net/problem/11779
import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = float('inf')
cost_info = [[] for _ in range(n)]
pre_table = [-1 for _ in range(n)]
min_dist_table = [INF for _ in range(n)]

for _ in range(m):
    start, end, cost = map(int, input().split(' '))
    cost_info[start - 1].append([end - 1, cost])
start_city, end_city = map(lambda x: int(x) - 1, input().split(' '))

queue = [(0, start_city, start_city)]
while queue:
    curr_cost, curr_city, prev_city = heapq.heappop(queue)
    if min_dist_table[curr_city] > curr_cost:
        min_dist_table[curr_city] = curr_cost
        pre_table[curr_city] = prev_city
    else:
        continue
    for next_city, next_cost in cost_info[curr_city]:
        heapq.heappush(queue, (curr_cost + next_cost, next_city, curr_city))

print(min_dist_table[end_city])
path_list = []
check_city = end_city
while pre_table[check_city] != start_city:
    path_list.append(str(check_city+1))
    check_city = pre_table[check_city]
path_list.append(str(check_city+1))
path_list.append(str(start_city+1))
print(len(path_list))
print(' '.join(reversed(path_list)))
