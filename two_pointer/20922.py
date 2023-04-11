# 겹치는 건 싫어 : https://www.acmicpc.net/problem/20922
N, K = map(int, input().split(' '))
N_list = list(map(int, input().split(' ')))
K_list = [0 for _ in range(100005)]

en = 0
result = 0
for st in range(N):
    while en < N and (K_list[N_list[en]] + 1) <= K:
        K_list[N_list[en]] += 1
        en += 1
    result = max(result, en - st)
    if en >= N:
        break
    K_list[N_list[st]] -= 1
print(result)
