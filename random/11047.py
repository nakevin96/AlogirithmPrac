# 동전 0 : https://www.acmicpc.net/problem/11047
from sys import stdin

input = stdin.readline
N, K = map(int, input().split(' '))
N_list = []
for _ in range(N):
    N_list.append(int(input()))
result = 0
for N_idx in range(N - 1, -1, -1):
    if N_list[N_idx] <= K:
        result += K // N_list[N_idx]
        K = K % N_list[N_idx]
    if K == 0:
        break
print(result)
