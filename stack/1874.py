from sys import stdin

s_input = stdin.readline

n = int(s_input())
stack1 = [i for i in range(n, 0, -1)]
stack2 = []
result = []

for _ in range(n):
    is_wrong = True
    num = int(s_input())
    while stack1 and stack1[-1] <= num:
        stack2.append(stack1.pop())
        result.append("+")
    if stack2 and stack2[-1] == num:
        is_wrong = False
        stack2.pop()
        result.append("-")
    if is_wrong:
        result = ["NO"]
        break

for r in result:
    print(r)
