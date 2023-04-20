# # 트리 순회: https://www.acmicpc.net/problem/1991
# import sys
#
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
#
# lc, rc = dict(), dict()
#
# N = int(input())
# for _ in range(N):
#     root, left_child, right_child = input().rstrip().split(' ')
#     lc[root] = left_child
#     rc[root] = right_child
#
# pre_order, in_order, post_order = '', '', ''
#
#
# def check_func(curr_node, check_type):
#     global pre_order, in_order, post_order
#     if check_type == 'PRE':
#         pre_order += curr_node
#     if lc[curr_node] != '.':
#         check_func(lc[curr_node], check_type)
#     if check_type == 'IN':
#         in_order += curr_node
#     if rc[curr_node] != '.':
#         check_func(rc[curr_node], check_type)
#     if check_type == 'POST':
#         post_order += curr_node
#
#
# check_func('A', 'PRE')
# check_func('A', 'IN')
# check_func('A', 'POST')
# print(pre_order)
# print(in_order)
# print(post_order)

# 트리 순회: https://www.acmicpc.net/problem/1991
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

lc, rc = [0 for _ in range(26)], [0 for _ in range(26)]
base = ord('A')
N = int(input())
for _ in range(N):
    root, left_child, right_child = input().rstrip().split(' ')
    lc[ord(root)-base] = ord(left_child)-base if left_child != '.' else -1
    rc[ord(root)-base] = ord(right_child)-base if right_child != '.' else -1

pre_order, in_order, post_order = '', '', ''


def check_func(curr_node, check_type):
    global pre_order, in_order, post_order
    if check_type == 'PRE':
        pre_order += chr(curr_node+base)
    if lc[curr_node] != -1:
        check_func(lc[curr_node], check_type)
    if check_type == 'IN':
        in_order += chr(curr_node+base)
    if rc[curr_node] != -1:
        check_func(rc[curr_node], check_type)
    if check_type == 'POST':
        post_order += chr(curr_node+base)


check_func(0, 'PRE')
check_func(0, 'IN')
check_func(0, 'POST')
print(pre_order)
print(in_order)
print(post_order)
