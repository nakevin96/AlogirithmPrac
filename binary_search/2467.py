# 용액 : https://www.acmicpc.net/problem/2467
import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().split(' ')))

# 투포인터 풀이
# left, right = 0, N - 1
# curr_val = abs(N_list[left] + N_list[right])
# curr_left, curr_right = left, right
# while left < right:
#     tmp_val = N_list[left] + N_list[right]
#     if abs(tmp_val) < curr_val:
#         curr_val = abs(tmp_val)
#         curr_left, curr_right = left, right
#
#     if tmp_val < 0:
#         left += 1
#     elif tmp_val > 0:
#         right -= 1
#     else:
#         break
# print(f'{N_list[curr_left]} {N_list[curr_right]}')

ans = float('INF')
ans_left, ans_right = 0, 0

for i in range(N-1):
    current = N_list[i]

    start = i + 1
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        tmp = current + N_list[mid]

        if abs(tmp) < ans:
            ans = abs(tmp)
            ans_left, ans_right = i, mid

        if tmp < 0:
            start = mid + 1
        elif tmp > 0:
            end = mid -1
        else:
            break
print(f'{N_list[ans_left]} {N_list[ans_right]}')
