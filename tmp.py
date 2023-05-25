def count_decodings(s):
    n = len(s)
    if n == 0:  # 빈 문자열일 경우 0을 반환합니다.
        return 0

    # dp[i]는 s[:i]까지의 문자열을 해석할 수 있는 경우의 수를 나타냅니다.
    dp = [0] * (n + 1)
    dp[0] = 1  # 빈 문자열을 해석할 수 있는 경우의 수는 1입니다.
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


# 입력을 받고 알고리즘을 호출합니다.
s = input("0~9 사이의 숫자로 이루어진 문자열을 입력하세요: ")
result = count_decodings(s)
print("주어진 입력은 {}가지의 문자열로 해석될 수 있습니다.".format(result))