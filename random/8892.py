# 팰린드롬 : https://www.acmicpc.net/problem/8892
# k개의 단어가 적혀있음 (서버 접속 비밀번호 힌트)
# k개의 단어 중 2개의 단어를 합쳐야 하며, 팰린드롬이어야 함
# 단어 k개 주어졌을 때, 팰린드롬 찾기
from sys import stdin
from itertools import permutations

input = stdin.readline


def get_permutations(w_list, count):
    if count == 0:
        return [[]]
    result = []
    for word_idx in range(len(w_list)):
        curr_word = w_list[word_idx]
        rest_item = [*w_list[:word_idx], *w_list[word_idx + 1:]]
        for rest in get_permutations(rest_item, count - 1):
            result.append([curr_word, *rest])
    return result


def is_palindrome(target_word):
    left, right = 0, len(target_word) - 1
    while left <= right:
        if target_word[left] != target_word[right]:
            return False
        left += 1
        right -= 1
    return True


T = int(input())

for _ in range(T):
    k = int(input())
    word_list = []
    for _ in range(k):
        word_list.append(input().rstrip())

    result = 0
    is_find = False
    for candidate_list in get_permutations(word_list, 2):
        if is_palindrome(''.join(candidate_list)):
            is_find = True
            print(''.join(candidate_list))
            break
    if not is_find:
        print(0)
