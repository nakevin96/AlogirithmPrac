import pprint
N, M, K = map(int, input().split(" "))
sticker_info_list = []
for _ in range(K):
    KR, KC = map(int, input().split(" "))
    curr_sticker_info = []
    for _ in range(KR):
        curr_sticker_info.append(list(map(int, input().split(" "))))
    sticker_info_list.append(curr_sticker_info)

notebook_info = [[0 for _ in range(M)] for _ in range(N)]


def rotate_matrix(matrix, turn):
    if turn == 0:
        return matrix
    row_len = len(matrix)
    col_len = len(matrix[0])
    rotate_result = [[0 for _ in range(row_len)] for _ in range(col_len)]
    for mr in range(row_len):
        for mc in range(col_len):
            rotate_result[mc][row_len - mr - 1] = matrix[mr][mc]
    return rotate_result


for sticker_info in sticker_info_list:
    for i in range(4):
        is_attached = False
        sticker_info = rotate_matrix(sticker_info, i)
        # 좌측 상단에서 시작해 우측으로 이동하며 스티커 붙일 공간이 있는지 판단
        for r_idx in range(N - len(sticker_info) + 1):
            if is_attached:
                break
            for c_idx in range(M - len(sticker_info[0]) + 1):
                is_valid = True
                for s_r_idx in range(len(sticker_info)):
                    for s_c_idx in range(len(sticker_info[0])):
                        if notebook_info[r_idx + s_r_idx][c_idx + s_c_idx] == 1 and sticker_info[s_r_idx][s_c_idx] == 1:
                            is_valid = False
                            break
                if is_valid:
                    for s_r_idx in range(len(sticker_info)):
                        for s_c_idx in range(len(sticker_info[0])):
                            if sticker_info[s_r_idx][s_c_idx] == 1:
                                notebook_info[r_idx + s_r_idx][c_idx + s_c_idx] = 1
                    is_attached = True
                    break
        if is_attached:
            break

result = 0
for nr in range(len(notebook_info)):
    for nc in range(len(notebook_info[0])):
        if notebook_info[nr][nc] == 1:
            result += 1

print(result)
