# 피보나치 수 2 : https://www.acmicpc.net/problem/2748
# 피보나치는 0과 1로 시작
# n번째 피보나치 수열 값을 구하는 함수 작성
n = int(input())
dp = [-1 for _ in range(n + 1)]
dp[0], dp[1] = 0, 1


def sol(num):
    if dp[num] == -1:
        tmp = sol(num - 1) + sol(num - 2)
        dp[num] = tmp
    return dp[num]


print(sol(n))
