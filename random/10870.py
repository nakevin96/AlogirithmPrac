# 피보나치 수 5 : https://www.acmicpc.net/problem/10870

N = int(input())
fibo_dp = {}
fibo_dp[0] = 0
fibo_dp[1] = 1
def fibo(n):
    if n not in fibo_dp:
        tmp_fibo_val = fibo(n-1) + fibo(n-2)
        fibo_dp[n] = tmp_fibo_val
    return fibo_dp[n]

print(fibo(N))
