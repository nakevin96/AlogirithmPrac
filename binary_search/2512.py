# 예산 : https://www.acmicpc.net/problem/2512

N = int(input())
N_list = list(map(int, input().split(' ')))
M = int(input())

low_cost, high_cost = 1, 100000
while low_cost < high_cost:
    mid_cost = (low_cost + high_cost + 1) // 2
    tmp_N = [n if n <= mid_cost else mid_cost for n in N_list]
    tmp_sum = sum(tmp_N)
    if tmp_sum <= M:
        low_cost = mid_cost
    else:
        high_cost = mid_cost - 1
print(low_cost if max(N_list) >= low_cost else max(N_list))
