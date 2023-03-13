# 팰린드롬? : https://www.acmicpc.net/problem/10942
import sys

input = sys.stdin.readline

N = int(input())
N_list = []
input_list = list(map(int, input().split(' ')))
for i in range(len(input_list)):
    N_list.append(-1)
    N_list.append(input_list[i])
N_list.append(-1)
N_len = len(N_list)
dp = [0 for _ in range(N_len)]

right, center = 0, 0

for i in range(N_len):
    if i >= right:
        center = right = i
        while right < N_len and right <= 2 * center and N_list[right] == N_list[2 * center - right]:
            right += 1
        right = right - 1
        dp[i] = right - center
    else:
        j = 2 * center - i
        if i + dp[j] < right:
            dp[i] = dp[j]
        elif i + dp[j] > right:
            dp[i] = right - i
        else:
            center = i
            while right < N_len and right <= 2 * center and N_list[right] == N_list[2 * center - right]:
                right += 1
            right = right - 1
            dp[i] = right - i

M = int(input())
for _ in range(M):
    start_idx, end_idx = map(int, input().split(' '))
    start_idx = 2 * start_idx - 1
    end_idx = 2 * end_idx - 1
    center = (start_idx + end_idx) // 2
    if dp[center] >= center - start_idx:
        print(1)
    else:
        print(0)
