import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())
N_list = list(map(int, input().split(' ')))
N_distinct_list = list(set(N_list))
N_distinct_len = len(N_distinct_list)
N_distinct_list.sort()
N_dict = dict()


def find_index(left, right, val):
    if left == right:
        return left
    mid = (left + right) // 2
    if N_distinct_list[mid] == val:
        return mid
    if N_distinct_list[mid] < val:
        return find_index(mid + 1, right, val)
    else:
        return find_index(left, mid - 1, val)


result = []
for n in N_list:
    if n not in N_dict:
        tmp = find_index(0, N_distinct_len - 1, n)
        N_dict[n] = tmp
    result.append(str(N_dict[n]))
print(' '.join(result))
