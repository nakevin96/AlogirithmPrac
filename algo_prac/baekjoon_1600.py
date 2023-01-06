from itertools import permutations
mr = [1, -1, 0, 0]
mc = [0, 0, 1, -1]
hr = [-2, -2, -1, -1, 1, 1, 2, 2]
hc = [-1, 1, -2, 2, -2, 2, -1, 1]

horse_move_limit = int(input())
col_len, row_len = tuple(map(int, input().split()))
map_info = []
for _r in range(row_len):
    map_info.append(list(map(int, input().split())))

total_monkey_move = row_len + col_len - 2
monkey_move = [0] * total_monkey_move
horse_move = [1] * horse_move_limit

monkey_move.extend(horse_move)
move_available_list = list(permutations(monkey_move, total_monkey_move - (3*horse_move_limit)))

for move_available in move_available_list:
    for move in move_available:
        pass