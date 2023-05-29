# 인간 대포: https://www.acmicpc.net/problem/10473
from sys import stdin
import heapq

input = stdin.readline


def get_distance(pos1, pos2):
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5


sourceX, sourceY = map(float, input().split(' '))
destX, destY = map(float, input().split(' '))

canon_num = int(input())
point_list = [[sourceX, sourceY]]
for _ in range(canon_num):
    point_list.append(list(map(float, input().split(' '))))
point_list.append([destX, destY])

# cost_info[i][j] = point i에서 point j까지 가는데 걸리는 최소 시간
cost_info = [[0 for _ in range(canon_num + 2)] for _ in range(canon_num + 2)]

for point_idx_1 in range(len(point_list)):
    for point_idx_2 in range(point_idx_1 + 1, len(point_list)):
        if point_idx_1 == 0:
            cost_info[point_idx_1][point_idx_2] = get_distance(point_list[point_idx_1], point_list[point_idx_2]) / 5
        else:
            distance = get_distance(point_list[point_idx_1], point_list[point_idx_2])
            cost_info[point_idx_1][point_idx_2] = min(distance / 5, 2 + (abs(distance - 50) / 5))

        cost_info[point_idx_2][point_idx_1] = cost_info[point_idx_1][point_idx_2]

MAX = float('inf')

# 원점에서 다른 점까지의 cost저장
distance_list = [MAX for _ in range(canon_num + 2)]
distance_list[0] = 0
heap = [[0, 0]]

while heap:
    curr_cost, curr_node = heapq.heappop(heap)
    if distance_list[curr_node] < curr_cost:
        continue

    for other_node in range(len(point_list)):
        if curr_node == other_node:
            continue
        if distance_list[other_node] > curr_cost + cost_info[curr_node][other_node]:
            distance_list[other_node] = curr_cost + cost_info[curr_node][other_node]
            heapq.heappush(heap, [distance_list[other_node], other_node])

print("%.6f" % (distance_list[canon_num + 1]))
