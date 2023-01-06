from sys import stdin

n = int(stdin.readline())

result = 0
for _ in range(n):
    string_list = list(stdin.readline().rstrip())
    stack = []
    for c in string_list:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        result += 1
print(result)
