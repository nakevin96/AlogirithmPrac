# 암호코드: https://www.acmicpc.net/problem/2011
# A: 65  / Z: 90
N = list(input())
N_len = len(N)
if N[0] == '0':
    print(0)
elif N_len == 1:
    print(1)
else:
    dp = [0 for _ in range(N_len + 1)]
    dp[0] = 1 if int(N[0]) > 0 else 0
    if N[1] == '0':
        if N[0] == '1' or N[0] == '2':
            dp[1] = 1
        else:
            dp[1] = 0
    else:
        if int(N[0] + N[1]) <= 26:
            dp[1] = 2
        else:
            dp[1] = 1

    flag = True
    for i in range(2, N_len):
        if N[i] == '0' and (N[i - 1] != '1' and N[i - 1] != '2'):
            flag = False
            break
        if int(N[i]) > 0:
            dp[i] += dp[i - 1]
        if int(N[i - 1]) > 0 and int(N[i - 1] + N[i]) <= 26:
            dp[i] += dp[i - 2]
    print(dp[N_len - 1] % 1000000 if flag else 0)
