# N = int(input())
# result = 0
# row_used_list = [-1 for _ in range(N)]
#
#
# def n_queen(target_col):
#     global result
#
#     def check_valid(check_col, check_row):
#         for _r_idx, _c_idx in enumerate(row_used_list):
#             if _c_idx == -1 or _c_idx == check_col:
#                 continue
#             if abs(check_col - _c_idx) == abs(check_row - _r_idx):
#                 return False
#         return True
#
#     if target_col == N:
#         result += 1
#         return
#     for r_idx in range(N):
#         if row_used_list[r_idx] == -1:
#             row_used_list[r_idx] = target_col
#             if check_valid(target_col, r_idx):
#                 n_queen(target_col + 1)
#             row_used_list[r_idx] = -1
#
#
# n_queen(0)
# print(result)

N = int(input())
used_row = [0 for _ in range(N)]
used_rising = [0 for _ in range(2 * N + 1)]
used_falling = [0 for _ in range(2 * N + 1)]
result = 0


def n_queen(col_idx):
    global result
    if col_idx == N:
        result += 1
        return

    for check_row in range(N):
        if used_row[check_row] or used_rising[check_row + col_idx] or used_falling[check_row - col_idx + N - 1]:
            continue
        used_row[check_row] = 1
        used_rising[check_row + col_idx] = 1
        used_falling[check_row - col_idx + N - 1] = 1
        n_queen(col_idx + 1)
        used_row[check_row] = 0
        used_rising[check_row + col_idx] = 0
        used_falling[check_row - col_idx + N - 1] = 0


n_queen(0)
print(result)
