# import heapq
#
# F, S, G, U, D = map(int, input().split(' '))
#
# queue = [(0, S)]
# visited = [float('inf') for _ in range(F + 1)]
#
# is_done = False
# while queue:
#     curr_point, curr_stair = heapq.heappop(queue)
#     if visited[curr_stair] < curr_point:
#         continue
#
#     if curr_stair == G:
#         is_done = True
#         print(curr_point)
#         break
#
#     if curr_stair - D > 0 and curr_point+1 < visited[curr_stair-D]:
#         visited[curr_stair - D] = curr_point + 1
#         heapq.heappush(queue, (curr_point + 1, curr_stair - D))
#     if curr_stair + U <= F and curr_point+1 < visited[curr_stair+U]:
#         visited[curr_stair + U] = curr_point + 1
#         heapq.heappush(queue, (curr_point + 1, curr_stair + U))
#
# if not is_done:
#     print('use the stairs')

from collections import deque

total_floor, start_floor, target_floor, up_move, down_move = map(int, input().split(' '))

queue = deque([[start_floor, 0]])
visited = [False for _ in range(total_floor + 1)]

is_done = False
while queue:
    curr_floor, curr_cost = queue.popleft()
    if curr_floor == target_floor:
        is_done = True
        print(curr_cost)
        break

    if curr_floor + up_move <= total_floor and not visited[curr_floor + up_move]:
        visited[curr_floor + up_move] = True
        queue.append([curr_floor + up_move, curr_cost + 1])
    if curr_floor - down_move > 0 and not visited[curr_floor - down_move]:
        visited[curr_floor - down_move] = True
        queue.append([curr_floor - down_move, curr_cost + 1])

if not is_done:
    print('use the stairs')
