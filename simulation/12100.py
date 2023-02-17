'''
첫째줄에 보드의 크기 N이 주어짐
그 다음부터 게임판의 초기상태가 주어진다 0은 빈칸 나머지는 해당 수에 해당하는 블록
5번 이동시켜 얻을 수 있는 가장 큰 블록을 출력한다.
'''
import copy
N = int(input())
max_val = 0
b_info = []
for n in range(N):
    b_info.append(list(map(int, input().split(" "))))
    for m in range(N):
        max_val = max(max_val, b_info[n][m])


def key_input(key, board_info):
    global max_val
    if key == 'right':
        for row_idx in range(N):
            count = 0
            selected_idx = N
            for col_idx in range(N - 1, -1, -1):
                if board_info[row_idx][col_idx] == 0:
                    continue
                if count == 0:
                    selected_idx = col_idx
                    count = 1
                elif count == 1:
                    if board_info[row_idx][selected_idx] == board_info[row_idx][col_idx]:
                        board_info[row_idx][selected_idx] *= 2
                        max_val = max(max_val, board_info[row_idx][selected_idx])
                        board_info[row_idx][col_idx] = 0
                        count = 0
                    else:
                        selected_idx = col_idx
                        count = 1
        for row_idx in range(N):
            for col_idx in range(N - 1, -1, -1):
                if board_info[row_idx][col_idx] > 0:
                    selected_idx = col_idx
                    while selected_idx < N - 1 and board_info[row_idx][selected_idx + 1] == 0:
                        board_info[row_idx][selected_idx + 1] = board_info[row_idx][selected_idx]
                        board_info[row_idx][selected_idx] = 0
                        selected_idx += 1
    elif key == 'down':
        for col_idx in range(N):
            count = 0
            selected_idx = N
            for row_idx in range(N - 1, -1, -1):
                if board_info[row_idx][col_idx] == 0:
                    continue
                if count == 0:
                    selected_idx = row_idx
                    count = 1
                elif count == 1:
                    if board_info[selected_idx][col_idx] == board_info[row_idx][col_idx]:
                        board_info[selected_idx][col_idx] *= 2
                        max_val = max(max_val, board_info[selected_idx][col_idx])
                        board_info[row_idx][col_idx] = 0
                        count = 0
                    else:
                        selected_idx = row_idx
                        count = 1
        for col_idx in range(N):
            for row_idx in range(N - 1, -1, -1):
                if board_info[row_idx][col_idx] > 0:
                    selected_idx = row_idx
                    while selected_idx < N - 1 and board_info[selected_idx + 1][col_idx] == 0:
                        board_info[selected_idx + 1][col_idx] = board_info[selected_idx][col_idx]
                        board_info[selected_idx][col_idx] = 0
                        selected_idx += 1
    elif key == 'left':
        for row_idx in range(N):
            count = 0
            selected_idx = -1
            for col_idx in range(N):
                if board_info[row_idx][col_idx] == 0:
                    continue
                if count == 0:
                    selected_idx = col_idx
                    count = 1
                elif count == 1:
                    if board_info[row_idx][selected_idx] == board_info[row_idx][col_idx]:
                        board_info[row_idx][selected_idx] *= 2
                        max_val = max(max_val, board_info[row_idx][selected_idx])
                        board_info[row_idx][col_idx] = 0
                        count = 0
                    else:
                        selected_idx = col_idx
                        count = 1
        for row_idx in range(N):
            for col_idx in range(N):
                if board_info[row_idx][col_idx] > 0:
                    selected_idx = col_idx
                    while selected_idx > 0 and board_info[row_idx][selected_idx - 1] == 0:
                        board_info[row_idx][selected_idx - 1] = board_info[row_idx][selected_idx]
                        board_info[row_idx][selected_idx] = 0
                        selected_idx -= 1
    elif key == 'up':
        for col_idx in range(N):
            count = 0
            selected_idx = -1
            for row_idx in range(N):
                if board_info[row_idx][col_idx] == 0:
                    continue
                if count == 0:
                    selected_idx = row_idx
                    count = 1
                elif count == 1:
                    if board_info[selected_idx][col_idx] == board_info[row_idx][col_idx]:
                        board_info[selected_idx][col_idx] *= 2
                        max_val = max(max_val, board_info[selected_idx][col_idx])
                        board_info[row_idx][col_idx] = 0
                        count = 0
                    else:
                        selected_idx = row_idx
                        count = 1
        for col_idx in range(N):
            for row_idx in range(N):
                if board_info[row_idx][col_idx] > 0:
                    selected_idx = row_idx
                    while selected_idx > 0 and board_info[selected_idx - 1][col_idx] == 0:
                        board_info[selected_idx - 1][col_idx] = board_info[selected_idx][col_idx]
                        board_info[selected_idx][col_idx] = 0
                        selected_idx -= 1
    else:
        print('wrong input')


def get_candidates(c_list, count):
    if count == 0:
        return [[]]
    result = []
    for idx in range(len(c_list)):
        item = c_list[idx]
        for rest in get_candidates(c_list[:], count - 1):
            result.append([item, *rest])
    return result


candidates = get_candidates(['right', 'down', 'left', 'up'], 5)
for c in candidates:
    copy_board = copy.deepcopy(b_info)
    for key in c:
        key_input(key, copy_board)
print(max_val)
