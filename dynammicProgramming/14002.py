# 가장 긴 증가하는 부분 수열 : https://www.acmicpc.net/problem/14002
import sys

input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split(' ')))

dp = [1 for _ in range(N)]
point = [i for i in range(N)]

for i in range(N-1, -1, -1):
    curr_point = i
    curr_dp = 0
    for j in range(i+1, N):
        if N_list[j] > N_list[i] and dp[j] > curr_dp:
            curr_dp = dp[j]
            curr_point = j
    dp[i] = curr_dp + 1
    point[i] = curr_point


max_dp = max(dp)
print(max_dp)
max_dp_idx = dp.index(max_dp)
result = []
while dp[max_dp_idx] > 1:
    result.append(str(N_list[max_dp_idx]))
    max_dp_idx = point[max_dp_idx]
result.append(str(N_list[max_dp_idx]))
print(' '.join(result))
