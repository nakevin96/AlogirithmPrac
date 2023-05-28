# 안정적인 문자열: https://www.acmicpc.net/problem/4889
from sys import stdin

input = stdin.readline
test_count = 1
while True:
    input_string = list(input().rstrip())
    if input_string[0] == '-':
        break

    stack = []
    result = 0

    for curly in input_string:
        if curly == '}':
            if stack:
                stack.pop()
            else:
                result += 1
                stack.append('{')
        elif curly == '{':
            stack.append('{')
        else:
            print('wrong input string. check input again')
    result += len(stack) // 2
    print(f'{test_count}. {result}')
    test_count += 1
