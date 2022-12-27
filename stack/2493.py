from sys import stdin

s_input = stdin.readline

n = int(s_input())
top_list = list(map(int, s_input().split(" ")))
stack = []
result = []

for idx in range(n):
    while stack and stack[-1][0] <= top_list[idx]:
        stack.pop()
    if stack:
        result.append(str(stack[-1][1]))
    else:
        result.append("0")
    stack.append((top_list[idx], idx+1))

print(" ".join(result))
