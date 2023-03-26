# 나무 자르기: https://www.acmicpc.net/problem/2805
N, M = map(int, input().split(' '))
tree_list = list(map(int, input().split(' ')))

min_height, max_height = 0, max(tree_list)

while min_height <= max_height:
    mid_height = (min_height + max_height + 1) // 2
    total_len = 0
    for t in tree_list:
        if t > mid_height:
            total_len += (t-mid_height)
    if total_len >= M:
        min_height = mid_height + 1
    else:
        max_height = mid_height - 1

print(max_height)
