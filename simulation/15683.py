import copy
N, M = map(int, input().split(" "))
office_info = []
cctv_dict = {
    1: (0, 1, 0, 0),
    11: (0, 0, 1, 0),
    111: (0, 0, 0, 1),
    1111: (1, 0, 0, 0),
    2: (0, 1, 0, 1),
    22: (1, 0, 1, 0),
    3: (1, 1, 0, 0),
    33: (0, 1, 1, 0),
    333: (0, 0, 1, 1),
    3333: (1, 0, 0, 1),
    4: (1, 1, 0, 1),
    44: (1, 1, 1, 0),
    444: (0, 1, 1, 1),
    4444: (1, 0, 1, 1),
    5: (1, 1, 1, 1)
}
office_list = []
for n in range(N):
    office_info.append(list(map(int, input().split(" "))))
    for m in range(M):
        if 5 >= office_info[n][m] >= 1:
            office_list.append((n, m, office_info[n][m]))


def get_candidates(c_list, count):
    if count == 0:
        return [[]]
    result = []
    for idx in range(len(c_list)):
        curr_cctv = c_list[idx]
        for rest in get_candidates(c_list[idx + 1:], count - 1):
            if curr_cctv[2] == 1:
                result.append([(curr_cctv[0], curr_cctv[1], 1), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 11), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 111), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 1111), *rest])
            elif curr_cctv[2] == 2:
                result.append([(curr_cctv[0], curr_cctv[1], 2), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 22), *rest])
            elif curr_cctv[2] == 3:
                result.append([(curr_cctv[0], curr_cctv[1], 3), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 33), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 333), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 3333), *rest])
            elif curr_cctv[2] == 4:
                result.append([(curr_cctv[0], curr_cctv[1], 4), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 44), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 444), *rest])
                result.append([(curr_cctv[0], curr_cctv[1], 4444), *rest])
            else:
                result.append([curr_cctv, *rest])
    return result


office_candidates = get_candidates(office_list, len(office_list))


def get_blind_spot(cctv_list, o_info):
    for cctv_info in cctv_list:
        [cr, cc, cctv_type] = cctv_info
        [d1, d2, d3, d4] = cctv_dict[cctv_type]
        if d1:
            nr = cr - 1
            while nr >= 0 and o_info[nr][cc] != 6:
                if o_info[nr][cc] == 0:
                    o_info[nr][cc] = -1
                nr -= 1
        if d2:
            nc = cc + 1
            while nc < M and o_info[cr][nc] != 6:
                if o_info[cr][nc] == 0:
                    o_info[cr][nc] = -1
                nc += 1
        if d3:
            nr = cr + 1
            while nr < N and o_info[nr][cc] != 6:
                if o_info[nr][cc] == 0:
                    o_info[nr][cc] = -1
                nr += 1
        if d4:
            nc = cc - 1
            while nc >= 0 and o_info[cr][nc] != 6:
                if o_info[cr][nc] == 0:
                    o_info[cr][nc] = -1
                nc -= 1
    result = 0
    for _n in range(N):
        for _m in range(M):
            if o_info[_n][_m] == 0:
                result += 1
    return result


problem_result = N * M
for oc in office_candidates:
    problem_result = min(problem_result, get_blind_spot(oc, copy.deepcopy(office_info)))
print(problem_result)
