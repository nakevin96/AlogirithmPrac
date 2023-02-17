from itertools import combinations

N, S = map(int, input().split(" "))

n_list = list(sorted(map(int, input().split(" "))))
result = 0

# def sol(curr_idx, curr_list):
#     global result
#     if curr_idx >= N:
#         return
#     if sum(curr_list) == S:
#         print(curr_list)
#         result += 1
#     if curr_list and sum(curr_list) > S:
#         return
#
#     for idx in range(curr_idx + 1, N):
#         sol(idx, [*curr_list, n_list[idx]])


for i in range(1, N+1):
    candidates = combinations(n_list, i)
    for c in candidates:
        if sum(c) == S:
            result += 1


print(result)
