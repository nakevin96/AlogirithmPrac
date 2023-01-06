from sys import stdin

while True:
    input_string = stdin.readline().rstrip()
    if input_string == ".":
        break

    stack = []
    is_valid = True

    for c in input_string:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if not stack or stack[-1] != "(":
                is_valid = False
                break
            stack.pop()
        elif c == "]":
            if not stack or stack[-1] != "[":
                is_valid = False
                break
            stack.pop()

    if stack:
        is_valid = False
    if is_valid:
        print("yes")
    else:
        print("no")
