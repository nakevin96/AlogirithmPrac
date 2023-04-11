import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
food_list = list(map(int, input().rstrip().split(' ')))
sum_list = [0 for _ in range(N + 1)]
for f_idx in range(N):
    sum_list[f_idx+1] = sum_list[f_idx] + food_list[f_idx]
count_sum_list = Counter(sum_list)
candidates = [count for val, count in count_sum_list.items() if count > 1]
result = 0
for c in candidates:
    result += (c*(c-1)) // 2
print(result)
