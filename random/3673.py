# https://www.acmicpc.net/problem/3673
import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    d, n = map(int, input().split(' '))
    num_list = list(map(int, input().split(' ')))
    mod = [0 for _ in range(d)]
    curr_sum = 0
    result = 0

    for num in num_list:
        curr_sum = (curr_sum + num) % d
        if curr_sum == 0:
            result += 1
        result += mod[curr_sum]
        mod[curr_sum] += 1
    print(result)