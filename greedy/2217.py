import sys
input = sys.stdin.readline
N = int(input())
weight_list = []
for _ in range(N):
    weight_list.append(int(input()))

weight_list.sort(reverse=True)
curr_weight = 0
for wi, w in enumerate(weight_list):
    next_weight = (wi+1) * w
    curr_weight = max(curr_weight, next_weight)

print(curr_weight)
