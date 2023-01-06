from sys import stdin

n = int(stdin.readline().rstrip())

for _ in range(n):
    string_list = list(stdin.readline().rstrip())
    stack = []
    is_valid = True
    for c in string_list:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                is_valid = False
                break

    if stack:
        is_valid = False
    if is_valid:
        print('YES')
    else:
        print('NO')

