# 문자열 집합: https://www.acmicpc.net/problem/14425
import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

MAX = (10000 * 500) + 5
root = 1
unused = 2
exist_check = [False for _ in range(MAX)]
next_node = [[-1 for _ in range(26)] for _ in range(MAX)]


def char_to_idx(target_char):
    return ord(target_char) - ord('a')


def insert(target_string):
    global unused
    curr_point = root
    for target_char in target_string:
        if next_node[curr_point][char_to_idx(target_char)] == -1:
            next_node[curr_point][char_to_idx(target_char)] = unused
            unused += 1
        curr_point = next_node[curr_point][char_to_idx(target_char)]
    exist_check[curr_point] = True


def find(target_string):
    curr_point = root
    for target_char in target_string:
        if next_node[curr_point][char_to_idx(target_char)] == -1:
            return False
        curr_point = next_node[curr_point][char_to_idx(target_char)]
    return exist_check[curr_point]


def erase(target_string):
    curr_point = root
    for target_char in target_string:
        if next_node[curr_point][char_to_idx(target_char)] == -1:
            return
        curr_point = next_node[curr_point][char_to_idx(target_char)]

    exist_check[curr_point] = False
    return


for _ in range(N):
    insert(input().rstrip())

result = 0
for _ in range(M):
    if find(input().rstrip()):
        result +=1
print(result)
