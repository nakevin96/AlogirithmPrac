# # 멀티버스 2 : https://www.acmicpc.net/problem/18869
# 틀렸음
# from collections import defaultdict
# M, N = map(int, input().split(' '))
# universe_dict = defaultdict(int)
# for _ in range(M):
#     input_universe = list(map(int, input().split(' ')))
#     input_universe = [(size, idx) for idx, size in enumerate(input_universe)]
#     input_universe.sort(key=lambda x: x[0])
#     key_list = [str(iu[1]) for iu in input_universe]
#     universe_dict[','.join(key_list)] += 1
#
#
# result = 0
# for val in universe_dict.values():
#     if val >= 2:
#         result += ((val * (val - 1)) // 2)
# print(result)

import sys

input = sys.stdin.readline

M, N = map(int, input().split(' '))
compressed_lists = []
for _ in range(M):
    tmp_list = list(map(int, input().split(' ')))
    sorted_list = sorted(list(set(tmp_list)))
    result = []
    for t in tmp_list:
        left, right = 0, len(sorted_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_list[mid] == t:
                result.append(mid)
                break
            if sorted_list[mid] < t:
                left = mid + 1
            else:
                right = mid - 1
    compressed_lists.append(result)

total = 0
for i in range(M-1):
    for j in range(i+1, M):
        is_done = True
        for k in range(N):
            if compressed_lists[i][k] != compressed_lists[j][k]:
                is_done = False
                break
        if is_done:
            total += 1
print(total)
