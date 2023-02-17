from collections import deque
from itertools import combinations
import pprint

N, M, G, R = map(int, input().split(" "))
result = 0

Ground_set = set()
Target_list = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for n in range(N):
    m_list = list(map(int, input().split(" ")))
    for m in range(len(m_list)):
        if m_list[m] == 1:
            Ground_set.add((n, m))
        elif m_list[m] == 2:
            Target_list.append((n, m))


def update_flower_num(start_list, target_set):
    global result
    flower_set = set()
    visited = [[["N", 0] for _c in range(M)] for _r in range(N)]
    for s in start_list:
        visited[s[0]][s[1]][0] = s[2]
    queue = deque(start_list)
    while queue:
        curr_r, curr_c, curr_color, curr_step = queue.popleft()
        if (curr_r, curr_c) in flower_set:
            continue

        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if (nr, nc) in target_set:
                if curr_color == "R" and visited[nr][nc][0] == "G" and visited[nr][nc][1] == curr_step + 1:
                    flower_set.add((nr, nc))
                    visited[nr][nc][0] = "F"

                elif visited[nr][nc][0] == "N":
                    visited[nr][nc] = [curr_color, curr_step + 1]
                    queue.append((nr, nc, curr_color, curr_step + 1))
    # if tmp_result > result:
    #     print("answer update: ")
    #     print(start_list)
    #     print(target_set)
    #     print(f"result/tmp_result : {result} / {tmp_result}")
    #     print(check)
    result = max(result, len(flower_set))


for g_candidate in combinations(Target_list, G):
    remaining = [t for t in Target_list if t not in g_candidate]
    for r_candidate in combinations(remaining, R):
        start_list = []
        check_set = set()
        for idx in range(G):
            start_list.append((g_candidate[idx][0], g_candidate[idx][1], "G", 0))
            check_set.add((g_candidate[idx][0], g_candidate[idx][1]))
        for idx in range(R):
            start_list.append((r_candidate[idx][0], r_candidate[idx][1], "R", 0))
            check_set.add((r_candidate[idx][0], r_candidate[idx][1]))
        remain_set = set([t for t in Target_list if t not in check_set])
        update_flower_num(start_list, Ground_set.union(remain_set))
print(result)
