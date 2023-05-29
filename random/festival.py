# algospot : festival https://www.algospot.com/judge/problem/read/FESTIVAL

from sys import stdin

input = stdin.readline

C = int(input())

for _ in range(C):
    N, L = map(int, input().split(' '))
    cost_list = list(map(int, input().rstrip().split(' ')))
    sum_list = [0 for _ in range(N + 1)]
    for cost_idx in range(N):
        sum_list[cost_idx + 1] = sum_list[cost_idx] + cost_list[cost_idx]

    result = float('inf')
    for start_idx in range(N):
        for count in range(L, N - start_idx + 1):
            tmp_result = (sum_list[start_idx+count] - sum_list[start_idx]) / count
            if tmp_result < result:
                result = tmp_result
    print(result)
