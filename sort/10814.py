import sys

input = sys.stdin.readline
N = int(input())


def merge(start, end):
    mid = (start + end) // 2
    a1, a2 = start, mid
    for ci in range(start, end):
        if a1 >= mid:
            tmp_list[ci] = people_list[a2]
            a2 += 1
        elif a2 >= end:
            tmp_list[ci] = people_list[a1]
            a1 += 1
        elif people_list[a1][0] <= people_list[a2][0]:
            tmp_list[ci] = people_list[a1]
            a1 += 1
        else:
            tmp_list[ci] = people_list[a2]
            a2 += 1
    for ci in range(start, end):
        people_list[ci] = tmp_list[ci]


def merge_sort(start, end):
    if start + 1 >= end:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid, end)
    merge(start, end)


people_list = list(map(lambda x: (int(x[0]), x[1]), [input().rstrip().split(" ") for _ in range(N)]))
tmp_list = [(0, '') for _ in range(N)]

merge_sort(0, N)
for p in people_list:
    print(f'{p[0]} {p[1]}')
