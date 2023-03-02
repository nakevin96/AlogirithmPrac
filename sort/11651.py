import sys

input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    tmp = input().split(" ")
    num_list.append((int(tmp[0]), int(tmp[1])))
tmp_list = [(0, 0) for i in range(N)]


def merge(start, end):
    mid = (start + end) // 2
    a1_idx, a2_idx = start, mid
    for t_idx in range(start, end):
        if a1_idx >= mid:
            tmp_list[t_idx] = num_list[a2_idx]
            a2_idx += 1
        elif a2_idx >= end:
            tmp_list[t_idx] = num_list[a1_idx]
            a1_idx += 1
        elif num_list[a1_idx][1] < num_list[a2_idx][1]:
            tmp_list[t_idx] = num_list[a1_idx]
            a1_idx += 1
        elif num_list[a1_idx][1] == num_list[a2_idx][1]:
            if num_list[a1_idx][0] <= num_list[a2_idx][0]:
                tmp_list[t_idx] = num_list[a1_idx]
                a1_idx += 1
            else:
                tmp_list[t_idx] = num_list[a2_idx]
                a2_idx += 1
        else:
            tmp_list[t_idx] = num_list[a2_idx]
            a2_idx += 1
    for t_idx in range(start, end):
        num_list[t_idx] = tmp_list[t_idx]


def merge_sort(ms, me):
    if ms + 1 >= me:
        return
    mid = (ms + me) // 2
    merge_sort(ms, mid)
    merge_sort(mid, me)
    merge(ms, me)


merge_sort(0, N)
for x, y in num_list:
    print(f'{x} {y}')
