seat_info = [list(input()) for _ in range(5)]


def check_is_adjacency(s_list):
    from collections import deque
    y_count = 0
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = [1 for _ in range(7)]
    queue = deque([s_list[0]])
    visited[0] = 0
    while queue:
        s = queue.popleft()
        s_r, s_c = s // 5, s % 5
        if seat_info[s_r][s_c] == 'Y':
            y_count += 1
        if y_count >= 4:
            return False
        for i in range(4):
            n_r = s_r + dr[i]
            n_c = s_c + dc[i]
            if n_r <0 or n_c < 0 or n_r >=5 or n_c >=5:
                continue
            if (n_r * 5) + n_c in s_list:
                next_idx = s_list.index(n_r * 5 + n_c)
                if visited[next_idx] == 1:
                    queue.append(n_r * 5 + n_c)
                    visited[next_idx] = 0

    return True if sum(visited) == 0 else False


result = 0
num_list = [i for i in range(25)]


def get_combination(n_list, select_num):
    if select_num == 0:
        return [[]]
    comb_result = []
    for idx in range(len(n_list)):
        item = n_list[idx]
        rest = n_list[idx + 1:]
        for tmp_result in get_combination(rest, select_num - 1):
            comb_result.append([item, *tmp_result])
    return comb_result


candidates = get_combination(num_list, 7)
for c in candidates:
    if check_is_adjacency(c):
        result += 1

print(result)

