# # 파티: https://www.acmicpc.net/problem/1238
#
# # N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 존재
#
# # M개의 단방향 도로, Ti 코스트 소모
#
# # 각 학생은 파티 장소에 갔다가 다시 돌아와야 하는데 최단 시간에 오고 가기를 원함
#
# # 가장 많은 시간을 소비하는 학생 구하기
# import heapq
# from sys import stdin
#
# input = stdin.readline
# INF = float('inf')
#
# student_num, road_num, target_vertex = map(int, input().split(' '))
# map_info = [[] for _ in range(student_num + 1)]
#
# for _ in range(road_num):
#     source, dest, cost = map(int, input().split(' '))
#     map_info[source].append([dest, cost])
#
#
# def get_dijkstra_list(start_vertex):
#     dijkstra_list = [INF for _ in range(student_num + 1)]
#     queue = [(0, start_vertex)]
#
#     while queue:
#         curr_cost, curr_vertex = heapq.heappop(queue)
#         if curr_cost >= dijkstra_list[curr_vertex]:
#             continue
#         dijkstra_list[curr_vertex] = curr_cost
#
#         for next_vertex, next_cost in map_info[curr_vertex]:
#             if curr_cost + next_cost < dijkstra_list[next_vertex]:
#                 heapq.heappush(queue, (curr_cost + next_cost, next_vertex))
#     return dijkstra_list
#
#
# target_to_rest_cost = get_dijkstra_list(target_vertex)
# result = 0
# for student_vertex in range(1, student_num + 1):
#     student_to_target_list = get_dijkstra_list(student_vertex)
#     result = max(result, student_to_target_list[target_vertex] + target_to_rest_cost[student_vertex])
# print(result)

# 파티: https://www.acmicpc.net/problem/1238

# N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 존재

# M개의 단방향 도로, Ti 코스트 소모

# 각 학생은 파티 장소에 갔다가 다시 돌아와야 하는데 최단 시간에 오고 가기를 원함

# 가장 많은 시간을 소비하는 학생 구하기
# import heapq
# from sys import stdin
#
# input = stdin.readline
# INF = float('inf')
#
# student_num, road_num, target_vertex = map(int, input().split(' '))
# dist_info = [[INF for _ in range(student_num + 1)] for _ in range(student_num + 1)]
# for student_vertex in range(1, student_num + 1):
#     dist_info[student_vertex][student_vertex] = 0
#
# for _ in range(road_num):
#     source, dest, cost = map(int, input().split(' '))
#     dist_info[source][dest] = cost
#
# for station in range(1, student_num + 1):
#     for source in range(1, student_num + 1):
#         for dest in range(1, student_num + 1):
#             dist_info[source][dest] = min(dist_info[source][dest],
#                                           dist_info[source][station] + dist_info[station][dest])
#
# result = 0
# for student_vertex in range(1, student_num+1):
#     result = max(result, dist_info[student_vertex][target_vertex] + dist_info[target_vertex][student_vertex])
# print(result)

# 가장 많은 시간을 소비하는 학생 구하기
import heapq
from sys import stdin

input = stdin.readline
INF = float('inf')

student_num, road_num, target_vertex = map(int, input().split(' '))
map_info = [[] for _ in range(student_num + 1)]
map_info_reverse = [[] for _ in range(student_num + 1)]

for _ in range(road_num):
    source, dest, cost = map(int, input().split(' '))
    map_info[source].append([dest, cost])
    map_info_reverse[dest].append([source, cost])


def get_dijkstra_list(start_vertex, is_reversed=False):
    selected_map = map_info_reverse if is_reversed else map_info
    dijkstra_list = [INF for _ in range(student_num + 1)]
    queue = [(0, start_vertex)]

    while queue:
        curr_cost, curr_vertex = heapq.heappop(queue)
        if curr_cost >= dijkstra_list[curr_vertex]:
            continue
        dijkstra_list[curr_vertex] = curr_cost

        for next_vertex, next_cost in selected_map[curr_vertex]:
            if curr_cost + next_cost < dijkstra_list[next_vertex]:
                heapq.heappush(queue, (curr_cost + next_cost, next_vertex))
    return dijkstra_list


target_to_rest_cost = get_dijkstra_list(target_vertex)
rest_to_target_cost = get_dijkstra_list(target_vertex, True)

result = 0
for student_vertex in range(1, student_num + 1):
    result = max(result, rest_to_target_cost[student_vertex] + target_to_rest_cost[student_vertex])
print(result)
