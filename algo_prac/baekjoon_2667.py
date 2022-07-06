def find_next(_row, _col):
    result = []
    if _row != 0:
        if house_map[_row-1][_col] != '0' and house_visited_map[_row-1][_col] == 0:
            result.append([_row-1, _col])
    if _row != size-1:
        if house_map[_row+1][_col] != '0' and house_visited_map[_row+1][_col] == 0:
            result.append([_row+1, _col])
    if _col != 0:
        if house_map[_row][_col-1] != '0' and house_visited_map[_row][_col-1] == 0:
            result.append([_row, _col-1])
    if _col != size-1:
        if house_map[_row][_col + 1] != '0' and house_visited_map[_row][_col + 1] == 0:
            result.append([_row, _col + 1])
    return result


size = int(input())

house_map = []
for _ in range(size):
    house_map.append(list(input()))

house_visited_map = [[0] * size for _ in range(size)]

label = 0
label_count_list = []
for row_idx in range(size):
    for col_idx in range(size):
        if house_map[row_idx][col_idx] != '0' and house_visited_map[row_idx][col_idx] == 0:
            label += 1
            count = 0
            stack = [[row_idx, col_idx]]
            while stack:
                curr = stack.pop()
                if house_visited_map[curr[0]][curr[1]] == 1:
                    continue
                count += 1
                house_map[curr[0]][curr[1]] = label
                house_visited_map[curr[0]][curr[1]] = 1
                next_visit_list = find_next(curr[0], curr[1])
                stack.extend(next_visit_list)
            label_count_list.append(count)

print(label)
label_count_list.sort()
for c in label_count_list:
    print(c)