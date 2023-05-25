# 암호코드 : https://www.acmicpc.net/problem/2011
from sys import stdin

input = stdin.readline

secret = input().rstrip()


def solve(input_string):
    input_len = len(input_string)
    # dp[i]는 input_string[i-1]까지만 사용해서 만들 수 있는 문자 갯수
    # 즉 dp[0]는 빈 문자열이니 1가지 방식으로만 해석됨
    dp = [0 for _ in range(input_len + 1)]
    dp[0] = 1

    # 만약 첫 문자가 0이면 해석 불가이므로 0 return
    if input_string[0] == '0':
        return 0
    dp[1] = 1

    for idx in range(1, input_len):
        checked = False
        if 1 <= int(input_string[idx]) <= 9:
            checked = True
            dp[idx+1] = (dp[idx+1] + dp[idx]) % 1000000
        if 10 <= int(input_string[idx - 1:idx + 1]) <= 26:
            checked = True
            dp[idx+1] = (dp[idx+1] + dp[idx - 1]) % 1000000
        if not checked:
            return 0

    return dp[input_len]


print(solve(secret))
