# 가운데서 만나기: https://www.acmicpc.net/problem/21940
import sys
input = sys.stdin.readline

CITY_NUM, ROAD_NUM = map(int, input().rstrip().split(' '))
map_info = [[float('inf') for _ in range(CITY_NUM)] for _ in range(CITY_NUM)]
for c in range(CITY_NUM):
    map_info[c][c] = 0

for _ in range(ROAD_NUM):
    city1, city2, move_cost = map(int, input().rstrip().split(' '))
    map_info[city1-1][city2-1] = move_cost

FRIEND_NUM = int(input())
living_city_list = list(map(lambda x: int(x)-1, input().rstrip().split(' ')))

for target_city in range(CITY_NUM):
    for start_city in range(CITY_NUM):
        for end_city in range(CITY_NUM):
            if map_info[start_city][end_city] > map_info[start_city][target_city] + map_info[target_city][end_city]:
                map_info[start_city][end_city] = map_info[start_city][target_city] + map_info[target_city][end_city]

result = [[-1], float('inf')]

for target_city in range(CITY_NUM):
    tmp_max_move_time = 0
    for living_city in living_city_list:
        tmp_move_time = map_info[living_city][target_city] + map_info[target_city][living_city]
        if tmp_max_move_time < tmp_move_time:
            tmp_max_move_time = tmp_move_time
    if result[1] > tmp_max_move_time:
        result = [[target_city], tmp_max_move_time]
    elif result[1] == tmp_max_move_time:
        result[0].append(target_city)

print(' '.join(list(map(lambda x: str(x+1), result[0]))))
