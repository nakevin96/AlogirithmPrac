N, M = map(int, input().split(" "))
info = {
    'empty': 0,
    'house': 1,
    'chicken_place': 2,
}
city_info = []
chicken_pos_list = []
house_pos_list = []
for r in range(N):
    city_info.append(list(map(int, input().split(" "))))
    for c in range(N):
        if city_info[r][c] == info['chicken_place']:
            chicken_pos_list.append((r, c))
        elif city_info[r][c] == info['house']:
            house_pos_list.append((r, c))


def get_candidates(c_list, count):
    if count == 0:
        return [[]]
    result = []
    for idx in range(len(c_list)):
        item = c_list[idx]
        for rest in get_candidates(c_list[idx + 1:], count - 1):
            result.append([item, *rest])
    return result


alive_chicken_place_list = get_candidates(chicken_pos_list, M)
result = 10000
for candidate in alive_chicken_place_list:
    house_dist_sum = 0
    for house_r, house_c in house_pos_list:
        min_dist = 100
        for chicken_place_r, chicken_place_c in candidate:
            min_dist = min(min_dist, abs(chicken_place_r-house_r) + abs(chicken_place_c-house_c))
        house_dist_sum += min_dist
    result = min(result, house_dist_sum)

print(result)
