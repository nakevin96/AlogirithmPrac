# 정수를 저장하는 스택 구현, 입력으로 주어지는 명령을 처리하는 프로그램
# push X: 정수 x를 스택에 넣는다
# pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1 아니면 0을 출력한다.
# top : 스택의 가장 위 정수를 출력한다.
from sys import stdin

s_Input = stdin.readline
stack = []

n = int(s_Input())
for _ in range(n):
    execution = s_Input().rstrip().split(" ")
    if len(execution) == 2:
        stack.append(execution[1])
    elif len(execution) == 1:
        if execution[0] == "pop":
            print(stack.pop() if stack else -1)
        elif execution[0] == "size":
            print(len(stack))
        elif execution[0] == "empty":
            print(0 if stack else 1)
        elif execution[0] == "top":
            print(stack[-1] if stack else -1)
        else:
            print("wrong command")
    else:
        print("wrong input")

