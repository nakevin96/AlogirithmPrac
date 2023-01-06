from sys import stdin

curl_list = list(stdin.readline().rstrip())
stack = list()


def check_valid():
    check_result = True
    tmp_stack = []
    for _c in curl_list:
        if _c == "(" or _c == "[":
            tmp_stack.append(_c)
        elif _c == ")":
            if tmp_stack and tmp_stack[-1] == "(":
                tmp_stack.pop()
            else:
                check_result = False
                break
        elif _c == "]":
            if tmp_stack and tmp_stack[-1] == "[":
                tmp_stack.pop()
            else:
                check_result = False
                break
    if stack:
        return False
    else:
        return check_result


if not check_valid():
    print("0")
else:
    for c in curl_list:
        if c == "(":
            stack.append("(")
        elif c == "[":
            stack.append("[")
        elif c == ")":
            if stack[-1].isdigit():
                tmp = 0
                while stack[-1].isdigit():
                    tmp += int(stack.pop())
                stack.pop()
                stack.append(str(2 * tmp))
            else:
                stack.pop()
                stack.append("2")
        elif c == "]":
            if stack[-1].isdigit():
                tmp = 0
                while stack[-1].isdigit():
                    tmp += int(stack.pop())
                stack.pop()
                stack.append(str(3 * tmp))
            else:
                stack.pop()
                stack.append("3")
    result = 0
    for s in stack:
        result += int(s)
    print(result)
