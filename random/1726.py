# 로봇 : https://www.acmicpc.net/problem/1726
from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().rstrip().split(' '))
map_info = []
for _ in range(R):
    map_info.append(list(map(int, input().rstrip().split(' '))))

start_r, start_c, start_direction = map(int, input().rstrip().split(' '))
end_r, end_c, end_direction = map(int, input().rstrip().split(' '))
start_r, start_c, end_r, end_c = start_r - 1, start_c - 1, end_r - 1, end_c - 1

DIRECT_POS_DICT = {
    1: (0, 1),
    2: (0, -1),
    3: (1, 0),
    4: (-1, 0)
}

DIRECT_VISITED_DICT = {
    1: 0,
    2: 1,
    3: 2,
    4: 3
}

TURN_RIGHT_DICT = {
    1: 3,
    3: 2,
    2: 4,
    4: 1
}

TURN_LEFT_DICT = {
    1: 4,
    4: 2,
    2: 3,
    3: 1,
}

visited = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]

# r, c, direction, cost
result = 0
queue = deque([(start_r, start_c, start_direction, 0)])
visited[start_r][start_c][DIRECT_VISITED_DICT[start_direction]] = True
while queue:
    curr_r, curr_c, curr_direction, curr_cost = queue.popleft()
    if (curr_r == end_r) and (curr_c == end_c) and (curr_direction == end_direction):
        result = curr_cost
        break
    turn_left_direction = TURN_LEFT_DICT[curr_direction]
    if not visited[curr_r][curr_c][DIRECT_VISITED_DICT[turn_left_direction]]:
        visited[curr_r][curr_c][DIRECT_VISITED_DICT[turn_left_direction]] = True
        queue.append((curr_r, curr_c, turn_left_direction, curr_cost + 1))
    turn_right_direction = TURN_RIGHT_DICT[curr_direction]
    if not visited[curr_r][curr_c][DIRECT_VISITED_DICT[turn_right_direction]]:
        visited[curr_r][curr_c][DIRECT_VISITED_DICT[turn_right_direction]] = True
        queue.append((curr_r, curr_c, turn_right_direction, curr_cost + 1))
    for straight_distance in range(1, 4):
        nr = curr_r + (DIRECT_POS_DICT[curr_direction][0] * straight_distance)
        nc = curr_c + (DIRECT_POS_DICT[curr_direction][1] * straight_distance)
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            break
        if map_info[nr][nc] == 1:
            break
        if not visited[nr][nc][DIRECT_VISITED_DICT[curr_direction]]:
            visited[nr][nc][DIRECT_VISITED_DICT[curr_direction]] = True
            queue.append((nr, nc, curr_direction, curr_cost + 1))
print(result)
