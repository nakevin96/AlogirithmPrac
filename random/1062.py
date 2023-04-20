# from sys import stdin
#
# input = stdin.readline
#
# # anta로 시작 tica로 끝남 -> antic 5개 무조건 들어가야 함
# # 즉 k가 5보다 작으면 0
#
# N, K = map(int, input().rstrip().split(' '))
# word_list = []
# for _ in range(N):
#     word_list.append(input().rstrip()[4:-4])
#
# # a~z 까지 배웠는지 체크
# alpha_check = [False for _ in range(26)]
# for needed in ['a', 'n', 't', 'i', 'c']:
#     alpha_check[ord(needed) - ord('a')] = True
#
# result = 0
#
#
# def dfs(k_count, alpha_idx):
#     global result
#     if k_count == K - 5:
#         # 다 배운 상태
#         tmp_result = 0
#         for word in word_list:
#             is_done = True
#             for c in word:
#                 if not alpha_check[ord(c) - ord('a')]:
#                     is_done = False
#                     break
#             if is_done:
#                 tmp_result += 1
#         result = max(result, tmp_result)
#         return
#     # 아직 다 안배운 상태
#     for idx in range(alpha_idx, 26):
#         if not alpha_check[idx]:
#             alpha_check[idx] = True
#             dfs(k_count + 1, idx + 1)
#             alpha_check[idx] = False
#
#
# if K < 5:
#     print(0)
# else:
#     dfs(0, 0)
#     print(result)
# https://www.acmicpc.net/problem/1062

def solve():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    result = 0

    alpa = {'a', 'n', 't', 'i', 'c'}

    total_need_alpa = {}
    alpa_list = []

    for i in range(N):
        split_alpa = sys.stdin.readline().strip()[4:-4]
        alpa_list.append(split_alpa)
        need_alpa = set()
        for cur_alpa in split_alpa:
            if cur_alpa not in alpa:
                need_alpa.add(cur_alpa)
        if not need_alpa:
            continue
        need_alpa = ''.join(sorted(list(need_alpa)))
        if need_alpa in total_need_alpa:
            total_need_alpa[need_alpa] += 1
        else:
            total_need_alpa[need_alpa] = 1

    if K < 5:
        print(result)
        return

    sorted_total_need_alpa = sorted(total_need_alpa.items(), key=lambda x: (x[0], x[1]), reverse=True)
    # print(sorted_total_need_alpa)

    cnt = 0
    for val, idx in sorted_total_need_alpa:
        for v in val:
            if cnt == K - 5:
                break
            if v not in alpa:
                alpa.add(v)
                cnt += 1

    for cur_word in alpa_list:
        is_add = True
        for cur_alpa in cur_word:
            if cur_alpa not in alpa:
                is_add = False
        if is_add:
            result += 1

    print(result)
    return

solve()
