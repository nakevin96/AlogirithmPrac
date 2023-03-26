# 선 긋기 : https://www.acmicpc.net/problem/2170
import sys

input = sys.stdin.readline

N = int(input())
dot_list = []
for _ in range(N):
    dot_list.append(list(map(int, input().split(' '))))

dot_list.sort(key=lambda x: (x[0], -x[1]))
result = 0
line_end = -1000000001
tmp_len = 0
for x1, x2 in dot_list:
    if x1 > line_end:
        result += tmp_len
        tmp_len = x2 - x1
        line_end = x2
    else:
        if line_end < x2:
            tmp_len += x2 - line_end
            line_end = x2
result += tmp_len

print(result)
