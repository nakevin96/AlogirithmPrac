import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    day = int(input())
    num_list = list(map(int, input().split(' ')))
    result = 0
    max_num = 0
    for num_idx in range(day-1, -1, -1):
        if max_num < num_list[num_idx]:
            max_num = num_list[num_idx]
        result += (max_num - num_list[num_idx])
    print(result)
