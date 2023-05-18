# # Boggle : https://www.acmicpc.net/problem/9202
# import sys
#
# input = sys.stdin.readline
# # Boggle에서는 상하좌우 대각선으로 이동가능
# dr = [1, -1, 0, 0, 1, 1, -1, -1]
# dc = [0, 0, 1, -1, 1, -1, 1, -1]
#
# # 글자 수에 따라 다른 점수 부여
# word_len_score = [0, 0, 0, 1, 1, 2, 3, 5, 11]
#
# # Tries 구현을 위한 변수들
# # MAX: 몇개의 노드가 존재할 수 있는가
# MAX = 300000 * 8 + 5
# ROOT_NODE_IDX = 1
# UNUSED_NODE_IDX = 2
#
# next_idx_table = [[-1 for _ in range(26)] for _ in range(MAX)]
# word_check_table = [0 for _ in range(MAX)]
# WORD_CHECK_FLAG = 2
#
#
# def insert_to_trie(target_string):
#     global UNUSED_NODE_IDX
#     curr_idx = ROOT_NODE_IDX
#     for target_char in target_string:
#         char_to_i = ord(target_char) - ord('A')
#         if next_idx_table[curr_idx][char_to_i] == -1:
#             next_idx_table[curr_idx][char_to_i] = UNUSED_NODE_IDX
#             UNUSED_NODE_IDX += 1
#         curr_idx = next_idx_table[curr_idx][char_to_i]
#     word_check_table[curr_idx] += 1
#
#
# def find_word_set(curr_string, curr_r, curr_c, node_idx):
#     if node_idx == -1:
#         return set()
#     result_set = set()
#     if word_check_table[node_idx] != 0 and word_check_table[node_idx] < WORD_CHECK_FLAG:
#         word_check_table[node_idx] = WORD_CHECK_FLAG
#         result_set.add(curr_string)
#
#     for i in range(8):
#         nr, nc = curr_r + dr[i], curr_c + dc[i]
#         if nr < 0 or nc < 0 or nr >= 4 or nc >= 4:
#             continue
#         if visited[nr][nc]:
#             continue
#         next_char = board[nr][nc]
#         visited[nr][nc] = True
#         result_set = result_set.union(
#             find_word_set(curr_string + next_char, nr, nc, next_idx_table[node_idx][ord(next_char) - ord('A')]))
#         visited[nr][nc] = False
#     return result_set
#
#
# # 1 < w < 300_000
# w = int(input())
# for _ in range(w):
#     # w개의 단어, len(단어) <= 8, 대문자 구성
#     input_string = input().rstrip()
#     insert_to_trie(input_string)
# input()
#
# # 1 < b < 30
# b = int(input())
#
# board = [['' for _ in range(4)] for _ in range(4)]
# visited = [[False for _ in range(4)] for _ in range(4)]
#
# for b_idx in range(b):
#     # boggle board 정보 받아서 board 초기화
#     for br in range(4):
#         board_row = input().rstrip()
#         for bc in range(4):
#             board[br][bc] = board_row[bc]
#
#     # 매 칸을 돌며 모든 가능한 답을 찾음
#     word_set = set()
#     for br in range(4):
#         for bc in range(4):
#             visited[br][bc] = True
#             word_set = word_set.union(
#                 find_word_set(board[br][bc], br, bc, next_idx_table[ROOT_NODE_IDX][ord(board[br][bc]) - ord('A')]))
#             visited[br][bc] = False
#     WORD_CHECK_FLAG += 1
#     word_list = [(len(word), word) for word in list(word_set)]
#     word_list.sort()
#     longest_word_len = word_list[-1][0]
#     score, longest_word, count = 0, '', len(word_list)
#     for w_len, w in word_list:
#         score += word_len_score[w_len]
#         if longest_word == '' and w_len == longest_word_len:
#             longest_word = w
#     print(f'{score} {longest_word} {count}')
#     if b_idx < b - 1:
#         input()

# Boggle: https://www.acmicpc.net/problem/9202

import sys

input = sys.stdin.readline

MAX = (300000 * 8) + 5
root = 1

unused = 2
mark = 2
exist_check = [0 for _ in range(MAX)]
next_node_idx = [[-1 for _ in range(26)] for _ in range(MAX)]
visited = [[0 for _ in range(4)] for _ in range(4)]
board = [['' for _ in range(4)] for _ in range(4)]
score = [0, 0, 0, 1, 1, 2, 3, 5, 11]
dr = [1, 0, -1, 0, 1, 1, -1, -1]
dc = [0, 1, 0, -1, 1, -1, 1, -1]


def insert(target_string):
    global unused
    curr_node_idx = root
    for t_ch in target_string:
        char_idx = ord(t_ch) - ord('A')
        if next_node_idx[curr_node_idx][char_idx] == -1:
            next_node_idx[curr_node_idx][char_idx] = unused
            unused += 1
        curr_node_idx = next_node_idx[curr_node_idx][char_idx]
    exist_check[curr_node_idx] = True


point = 0
word_count = 0
max_string = ''


def find(curr_r, curr_c, node_idx, target_string):
    global point, word_count, max_string
    if node_idx == -1:
        return

    if exist_check[node_idx] != 0 and exist_check[node_idx] != mark:
        exist_check[node_idx] = mark
        point += score[len(target_string)]
        word_count += 1
        if len(target_string) > len(max_string):
            max_string = target_string
        elif (len(target_string) == len(max_string)) and target_string < max_string:
            max_string = target_string

    for i in range(8):
        nr, nc = curr_r + dr[i], curr_c + dc[i]
        if nr < 0 or nc < 0 or nr >= 4 or nc >= 4:
            continue
        if visited[nr][nc] == 1:
            continue
        next_char = board[nr][nc]
        visited[nr][nc] = 1
        find(nr, nc, next_node_idx[node_idx][ord(next_char) - ord('A')], target_string + next_char)
        visited[nr][nc] = 0


def solve():
    global point, word_count, max_string, mark
    point = 0
    word_count = 0
    max_string = ''

    for r in range(4):
        for c in range(4):
            visited[r][c] = 1
            find(r, c, next_node_idx[root][ord(board[r][c]) - ord('A')], board[r][c])
            visited[r][c] = 0

    print(f'{point} {max_string} {word_count}')
    mark += 1


w = int(input())
for _ in range(w):
    insert(input().rstrip())
input()

b = int(input())
for bi in range(b):
    visited = [[0 for _ in range(4)] for _ in range(4)]
    board = [['a' for _ in range(4)] for _ in range(4)]
    for br in range(4):
        tmp_board_row = input().rstrip()
        for bc in range(4):
            board[br][bc] = tmp_board_row[bc]
    solve()
    if bi < b - 1:
        input()
