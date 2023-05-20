import sys

input = sys.stdin.readline

N = int(input())
N_list = []
for _ in range(N):
    N_list.append(int(input()))
N_len = len(N_list)

# bubble sort
for level in range(N_len-2, -1, -1):
    for target in range(level+1):
        if N_list[target] > N_list[target+1]:
            N_list[target], N_list[target+1] = N_list[target+1], N_list[target]
print(N_list)