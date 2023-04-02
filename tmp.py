import sys

input = sys.stdin.readline
N = int(input())
N_list = []
for _ in range(N):
    N_list.append(int(input()))
N_list.sort()

two_sum = set()
for n1 in range(N):
    for n2 in range(N):
        two_sum.add(N_list[n1] + N_list[n2])

two_sum = sorted(list(two_sum))
tow_sum_len = len(two_sum)

is_done = False
for n1 in range(N - 1, -1, -1):
    if is_done:
        break
    for n2 in range(n1 + 1):
        left, right = 0, tow_sum_len - 1
        while left <= right:
            mid = (left + right) // 2
            if two_sum[mid] == N_list[n1] - N_list[n2]:
                is_done = True
                print(N_list[n1])
                break
            if two_sum[mid] < N_list[n1] - N_list[n2]:
                left = mid + 1
            else:
                right = mid - 1
        if is_done:
            break
