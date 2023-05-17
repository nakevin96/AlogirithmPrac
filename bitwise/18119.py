# 단어 암기 : https://www.acmicpc.net/problem/18119
import sys

input = sys.stdin.readline

# N: 체크해야 하는 문자열 수, M: 기억관련 명령어 수
N, M = map(int, input().split(' '))


# 들어오는 input을 알파벳 26에 맞춰서 2진수로 바꾸면 어떨까??

def get_alpha_index(target_alpha):
    return ord(target_alpha) - ord('a')


def get_shift_count(target_alpha):
    return 25 - (ord(target_alpha) - ord('a'))


remember_binary = (2 ** 26) - 1
alpha_to_binary_list = []
for _ in range(N):
    input_word = input().rstrip()
    alpha_list = [0 for _ in range(26)]
    for alpha in input_word:
        alpha_list[get_alpha_index(alpha)] = 1
    alpha_num = 0
    for alpha_idx in range(26):
        if alpha_list[alpha_idx] == 1:
            alpha_num += 2 ** (25 - alpha_idx)
    alpha_to_binary_list.append(alpha_num)

for _ in range(M):
    command, target = input().rstrip().split(' ')
    if command == '1':
        remember_binary = remember_binary & (~(1 << get_shift_count(target)))
    elif command == '2':
        remember_binary = remember_binary | (1 << get_shift_count(target))
    else:
        print("error input after 35 line")
        break

    print_result = 0
    for alpha_binary in alpha_to_binary_list:
        if (alpha_binary & remember_binary) == alpha_binary:
            print_result += 1
    print(print_result)
