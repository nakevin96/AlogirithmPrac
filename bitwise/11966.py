# 2의 제곱인가? https://www.acmicpc.net/problem/11966

N = int(input())
result = 1
while N > 1:
    if N % 2 != 0:
        result = 0
        break
    N = N // 2
print(result)

