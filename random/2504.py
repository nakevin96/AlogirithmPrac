# 괄호의 값: https://www.acmicpc.net/problem/2504
def is_valid(brace_list):
    stack = []
    for b in brace_list:
        if b == '(' or b == '[':
            stack.append(b)
        elif b == ')':
            if not stack:
                return False
            target = stack.pop()
            if target != '(':
                return False
        elif b == ']':
            if not stack:
                return False
            target = stack.pop()
            if target != '[':
                return False
    if stack:
        return False
    return True


b_list = list(input())
if not is_valid(b_list):
    print(0)
else:
    result = 0
    stack = []
    for b in b_list:
        if b == '(' or b == '[':
            stack.append(b)
        elif b == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                tmp = stack.pop()
                stack.pop()
                tmp *= 2
                stack.append(tmp)
        elif b == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                tmp = stack.pop()
                stack.pop()
                tmp *= 3
                stack.append(tmp)
        tmp_sum = 0
        while stack and (stack[-1] != '(' and stack[-1] != '['):
            tmp_sum += stack.pop()
        if stack and tmp_sum > 0:
            stack.append(tmp_sum)
        else:
            result += tmp_sum
    print(result)
#

# def solve():
#     import sys
#
#     value = list(sys.stdin.readline().strip())
#     stack = []
#     result = 0
#     temp = 1
#
#     for i in range(len(value)):
#         if value[i] == "(":
#             stack.append(value[i])
#             temp *= 2
#         elif value[i] == "[":
#             stack.append(value[i])
#             temp *= 3
#         else:
#             if value[i] == ")":
#                 if not stack or stack[-1] == "[":
#                     result = 0
#                     break
#                 if value[i-1] == "(":
#                     result += temp
#                 stack.pop()
#                 temp //= 2
#             else:
#                 if not stack or stack[-1] == "(":
#                     result = 0
#                     break
#                 if value[i-1] == "[":
#                     result += temp
#                 stack.pop()
#                 temp //= 3
#
#     if stack:
#         print(0)
#     else:
#         print(result)
#
# solve()