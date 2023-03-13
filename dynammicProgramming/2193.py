# 이친수 : https://www.acmicpc.net/problem/2193
n = int(input())

dp_zero = [0 for _ in range(100)]
dp_one = [0 for _ in range(100)]
dp_zero[1], dp_one[1] = 0, 1
if n == 1:
    print(1)
else:
    for check in range(2, n+1):
        dp_zero[check] = dp_zero[check-1] + dp_one[check-1]
        dp_one[check] = dp_zero[check-1]

    print(dp_zero[n] + dp_one[n])
