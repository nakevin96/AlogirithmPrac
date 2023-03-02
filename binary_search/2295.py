import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
N_list = []
for _ in range(N):
    N_list.append(int(input()))
N_list.sort()

N2_list = []
for n1_idx in range(N):
    for n2_idx in range(n1_idx, N):
        N2_list.append(N_list[n1_idx] + N_list[n2_idx])
N2_list.sort()
N2_len = len(N2_list)


def find_val(left, right, val):
    if left > right:
        return False
    mid = (left + right) // 2
    if N2_list[mid] == val:
        return True
    if N2_list[mid] < val:
        return find_val(mid + 1, right, val)
    else:
        return find_val(left, mid - 1, val)


def sol():
    for n1 in range(N - 1, 0, -1):
        for n2 in range(n1):
            if find_val(0, N2_len - 1, N_list[n1] - N_list[n2]):
                return N_list[n1]


print(sol())
