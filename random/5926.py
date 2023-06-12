from sys import stdin

input = stdin.readline

num_of_cows = int(input())

info_list = []
breed_set = set()
breed_count_dict = dict()
for _ in range(num_of_cows):
    x_pos, breed_id = map(int, input().rstrip().split(' '))
    breed_set.add(breed_id)
    breed_count_dict[breed_id] = 0
    info_list.append([x_pos, breed_id])

info_list.sort(key=lambda x: x[0])

end = 0
info_len = len(info_list)

breed_count_dict[info_list[0][1]] += 1
breed_count_set = set()
breed_count_set.add(info_list[0][1])
breed_set_limit = len(breed_set)

result = float('inf')
for start in range(info_len):
    while (end < info_len) and (len(breed_count_set) < breed_set_limit):
        end += 1
        if end >= info_len:
            break

        breed_count_set.add(info_list[end][1])
        breed_count_dict[info_list[end][1]] += 1

    if end >= info_len:
        break

    # 여기까지 오면 end가 info_len보다 작고, 모든 종류의 소의 품종을 찍을 수 있는 상태
    result = min(result, info_list[end][0]-info_list[start][0])

    breed_count_dict[info_list[start][1]] -= 1
    if breed_count_dict[info_list[start][1]] == 0:
        breed_count_set.remove(info_list[start][1])

print(result)
