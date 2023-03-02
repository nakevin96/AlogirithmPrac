import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
n_list = []
tmp_list = [0 for _ in range(N)]
for _ in range(N):
    n_list.append(int(input()))


def merge(s, e):
    m = (s + e) // 2
    m1_idx, m2_idx = s, m
    for t in range(s, e):
        if m1_idx == m:
            tmp_list[t] = n_list[m2_idx]
            m2_idx += 1
        elif m2_idx == e:
            tmp_list[t] = n_list[m1_idx]
            m1_idx += 1
        elif n_list[m1_idx] <= n_list[m2_idx]:
            tmp_list[t] = n_list[m1_idx]
            m1_idx += 1
        else:
            tmp_list[t] = n_list[m2_idx]
            m2_idx += 1

    for t in range(s, e):
        n_list[t] = tmp_list[t]


def merge_sort(s, e):
    if s + 1 == e:
        return
    m = (s + e) // 2
    merge_sort(s, m)
    merge_sort(m, e)
    merge(s, e)


merge_sort(0, N)
for r in range(0, N):
    print(n_list[r])
