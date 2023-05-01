def solution(n):
    dp = [0 for _ in range(n + 2)]
    dp[0], dp[1], dp[2], dp[3] = 1, 1, 3, 10
    if n <= 3:
        return dp[n]
    for k in range(4, n + 1):
        pattern_sum = [0 for _ in range(3)]
        dp[k] = (dp[k - 1] + (dp[k - 2] * 2) + (dp[k - 3] * 5)) % 1000000007
        remain = k - 4
        while remain >= 0:
            pattern_sum[(k - remain) % 3] += dp[remain]
            remain -= 1
        dp[k] = (dp[k] + (pattern_sum[0] * 4)) % 1000000007
        dp[k] = (dp[k] + (pattern_sum[1] * 2)) % 1000000007
        dp[k] = (dp[k] + (pattern_sum[2] * 2)) % 1000000007
    return dp[n]


print(solution(6))
