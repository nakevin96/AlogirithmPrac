# 좋다: https://www.acmicpc.net/problem/1253
N = int(input())
N_list = list(map(int, input().split(' ')))
N_list.sort()

result = 0
two_sum = []
for i in range(N - 1):
    for j in range(i + 1, N):
        two_sum.append((N_list[i] + N_list[j], i, j))
two_sum.sort(key=lambda x: x[0])
two_sum_len = len(two_sum)

for idx in range(N):
    target = N_list[idx]
    l1, l2, r1, r2 = 0, 0, two_sum_len, two_sum_len
    while l1 < r1:
        mid = (l1 + r1) // 2
        if two_sum[mid][0] >= target:
            r1 = mid
        else:
            l1 = mid + 1
    while l2 < r2:
        mid = (l2 + r2) // 2
        if two_sum[mid][0] <= target:
            l2 = mid + 1
        else:
            r2 = mid
    is_find = False
    for t in range(r1, r2):
        if idx != two_sum[t][1] and idx != two_sum[t][2]:
            is_find = True
            break
    if is_find:
        result += 1
print(result)
