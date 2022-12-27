from sys import stdin

s_input = stdin.readline

n = int(s_input())
result = ["-1" for _ in range(n)]
stack = []
num_list = list(map(int, s_input().split(" ")))

for i in range(n):
    while stack and stack[-1][0] < num_list[i]:
        tmp_num, tmp_idx = stack.pop()
        result[tmp_idx] = str(num_list[i])
    stack.append((num_list[i], i))

print(" ".join(result))

