# 가장 긴 증가하는 부분 수열 2 : https://www.acmicpc.net/problem/12015
N = int(input())
A_list = list(map(int, input().split(' ')))
# dp = [1 for _ in range(N)]
#
# for idx in range(N-1, -1, -1):
#     for post_idx in range(idx+1, N):
#         if A_list[idx] < A_list[post_idx] and dp[idx] <= dp[post_idx]:
#             dp[idx] = dp[post_idx] + 1
# print(max(dp))
long_list = []
for a in A_list:
    if long_list and a <= long_list[-1]:
        # 이분탐색
        left, right = 0, len(long_list)
        while left < right:
            mid = (left + right) // 2
            if long_list[mid] < a:
                left = mid + 1
            else:
                right = mid
        long_list[left] = a
    else:
        long_list.append(a)
print(len(long_list))
