# 부분합 : https://www.acmicpc.net/problem/1806
import sys

input = sys.stdin.readline

N, S = map(int, input().rstrip().split(' '))
N_list = list(map(int, input().rstrip().split(' ')))


# 투포인터 풀이
# ep = 0
# result = N+1
# curr_sum = N_list[0]
#
# for sp in range(N):
#     while ep < N and curr_sum < S:
#         ep += 1
#         if ep != N:
#             curr_sum += N_list[ep]
#     if ep == N:
#         break
#     result = min(result, ep-sp+1)
#     curr_sum -= N_list[sp]
#
# if result == N+1:
#     print(0)
# else:
#     print(result)

# 이분 탐색 풀이
def check(length):
    # check if there exists a subsequence of length 'length'
    # whose sum is greater than or equal to S
    curr_sum = sum(N_list[:length])
    if curr_sum >= S:
        return True
    for i in range(length, N):
        curr_sum += N_list[i] - N_list[i - length]
        if curr_sum >= S:
            return True
    return False


# perform binary search to find the smallest length
# for which the check function returns True
lo, hi = 1, N
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

if ans == 0:
    print(0)
else:
    print(ans)
