from sys import stdin

HEIGHT = 0
IDX = 1

while True:
    test_case = list(map(int, stdin.readline().split(" ")))
    n = test_case.pop(0)
    if n == 0:
        break

    stack = []
    result = 0

    for idx in range(n):
        while stack and stack[-1][HEIGHT] > test_case[idx]:
            tmp_height, tmp_idx = stack.pop()
            width = idx if not stack else idx - stack[-1][IDX] - 1
            result = max(result, width * tmp_height)
        stack.append((test_case[idx], idx))

    while stack:
        tmp_height, tmp_idx = stack.pop()
        width = n if not stack else n - stack[-1][IDX] - 1
        result = max(result, width * tmp_height)

    print(result)
