from collections import deque
from collections import defaultdict


def solution():
    result = 0
    count_dict = defaultdict(int)
    col_len, row_len = map(int, input().split())
    start_point = []
    box_info = []
    for _r in range(row_len):
        tmp_list = list(map(int, input().split()))
        box_info.append(tmp_list)
        for t_idx in range(col_len):
            count_dict[tmp_list[t_idx]] += 1
            if tmp_list[t_idx] == 1:
                start_point.append((_r, t_idx))

    if (row_len * col_len) - count_dict[-1] == count_dict[1]:
        return 0
    visited = [[0 for _c in range(col_len)] for _r in range(row_len)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    def bfs():
        nonlocal visited
        count = 0
        queue = deque()
        queue.extend(start_point)
        for _q in queue:
            visited[_q[0]][_q[1]] = 1
        while queue:
            curr_r, curr_c = queue.popleft()
            for i in range(4):
                nr = curr_r + dr[i]
                nc = curr_c + dc[i]
                if nr < 0 or nr >= row_len or nc < 0 or nc >= col_len:
                    continue
                elif box_info[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[curr_r][curr_c] + 1
                    count = max(count, visited[nr][nc])
                    queue.append((nr, nc))
        return count - 1

    result = bfs()
    for _r in range(row_len):
        for _c in range(col_len):
            if visited[_r][_c] == 0 and box_info[_r][_c] == 0:
                return -1
    return result


print(solution())
