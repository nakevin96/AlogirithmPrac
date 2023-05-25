import sys

input = sys.stdin.readline

N = int(input())
N_count = dict()
for _ in range(N):
    input_n = int(input())
    if input_n not in N_count:
        N_count[input_n] = 1
    else:
        N_count[input_n] += 1

sorted_n_list = sorted([(count, -1*n_num) for n_num, count in N_count.items()])
print(-1 * sorted_n_list[-1][1])
