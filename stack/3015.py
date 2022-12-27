from sys import stdin
HEIGHT, CNT = 0, 1

N = int(stdin.readline())
heights = [int(stdin.readline()) for _ in range(N)]

stack = []
answer = 0

for h in heights:
    while stack and stack[-1][HEIGHT] < h:
        answer += stack.pop()[CNT]

    if not stack:
        stack.append([h, 1])
        continue

    if stack[-1][HEIGHT] == h:
        answer += stack[-1][CNT]
        stack[-1][CNT] += 1

        if len(stack) > 1:
            answer += 1
    else:
        stack.append([h, 1])
        answer += 1
print(answer)
