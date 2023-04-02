# 휴게소 세우기: https://www.acmicpc.net/problem/1477
# 처음에 가장 긴 구간을 절반으로 나누어 가며 최소거리를 구하려 했는데
# 예외 케이스가 존재, 틀린 접근 ( 가장 긴 구간을 절반이 아닌 2.5 : 1 처럼 잘라서 나중에 더 작은 값을 만들어낼 수 있음)

# import heapq
#
# N, M, L = map(int, input().split(' '))
# exist_list = [0]
# exist_list.extend(list(map(int, input().split(' '))))
# exist_list.append(L)
# exist_list.sort()
# queue = []
# for e1, e2 in zip(exist_list, exist_list[1:]):
#     heapq.heappush(queue, (e1 - e2, e1, e2))
#
# count = 0
# while count < M:
#     curr_dist, left, right = heapq.heappop(queue)
#     curr_dist *= -1
#     if curr_dist == 1:
#         continue
#     mid = (left + right) // 2
#     heapq.heappush(queue, (left - mid, left, mid))
#     heapq.heappush(queue, (mid - right, mid, right))
#     count += 1
#
# result = heapq.heappop(queue)
# print(-result[0])
import sys

N, M, L = map(int, sys.stdin.readline().rstrip().split(' '))
exist_list = [0]
if N > 0:
    N_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    exist_list.extend(N_list)
exist_list.append(L)
exist_list.sort()
interval = []
for i in range(1, len(exist_list)):
    interval.append(exist_list[i] - exist_list[i - 1])

st, en = 1, L - 1
while st < en:
    mid = (st + en) // 2
    tmp = 0
    for d in interval:
        if d > mid:
            tmp += (d - 1) // mid
    if tmp > M:
        st = mid + 1
    else:
        en = mid
print(en)
