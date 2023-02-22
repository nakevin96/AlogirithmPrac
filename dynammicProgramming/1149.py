import sys

input = sys.stdin.readline
house_num = int(input())
cost_list = [[0, 0, 0]]
for _ in range(house_num):
    cost_list.append(list(map(int, input().split(" "))))
dp = [[0 for _color in range(3)] for _ in range(house_num+1)]
for house_idx in range(1, house_num+1):
    for color_idx in range(3):
        min_cost = 1000001
        for before_color_idx in range(3):
            if before_color_idx == color_idx:
                continue
            min_cost = min(min_cost, dp[house_idx-1][before_color_idx])
        dp[house_idx][color_idx] = min_cost + cost_list[house_idx][color_idx]
print(min([dp[house_num][ci] for ci in range(3)]))
