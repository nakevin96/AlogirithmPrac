# 가장 긴 증가하는 부분 수열 (연속 X):https://www.acmicpc.net/problem/11053
# 1 <= N <= 1000
# 뒤에서 부터 체크하며 가장 길게 연결할 수 있는 수를 max_len_list에 저
N = int(input())
N_list = list(map(int, input().split(' ')))
max_len_list = [0 for _ in range(N)]

for check_idx in range(N-1, -1, -1):
    max_len = 0
    for follower_item_idx in range(check_idx+1, N):
        if (N_list[check_idx] < N_list[follower_item_idx]) and max_len_list[follower_item_idx] > max_len:
            max_len = max_len_list[follower_item_idx]
    max_len_list[check_idx] = max_len + 1

print(max(max_len_list))