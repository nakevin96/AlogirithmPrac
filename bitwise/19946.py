# 2의 제곱수 계산하기: https://www.acmicpc.net/problem/19946
check_num = int(input())
result = 64
while check_num % 2 == 0:
    check_num //= 2
    result -= 1
print(result)

