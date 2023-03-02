import sys

input = sys.stdin.readline
N = int(input())
flower_list = []
month_day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_dict = [0]
for m in range(1, 13):
    month_dict.append(sum(month_day_list[:m]))
garden_open = month_dict[3] + 1
garden_end = month_dict[11] + 30
for _ in range(N):
    start_month, start_day, end_month, end_day = map(int, input().split(' '))
    flower_list.append((month_dict[start_month] + start_day, month_dict[end_month] + end_day))
flower_list.sort(key=lambda x: -x[1])
result = 0
curr_idx = 0
base = garden_end + 1
next_base = garden_end + 1

while curr_idx < N:
    is_find = False
    while curr_idx < N and flower_list[curr_idx][1] >= base:
        is_find = True
        if flower_list[curr_idx][0] < next_base:
            next_base = flower_list[curr_idx][0]
        curr_idx += 1
    if not is_find:
        break
    else:
        result += 1
        base = next_base
        if base <= garden_open:
            break

if base > garden_open:
    print(0)
else:
    print(result)
