sentence1 = list(input())
sentence2 = list(input())

dp = [[0 for _ in range(len(sentence1) + 1)] for _ in range(len(sentence2) + 1)]
for s2_plus_idx in range(1, len(sentence2) + 1):
    for s1_plus_idx in range(1, len(sentence1) + 1):
        if sentence1[s1_plus_idx - 1] == sentence2[s2_plus_idx-1]:
            dp[s2_plus_idx][s1_plus_idx] = dp[s2_plus_idx - 1][s1_plus_idx - 1] + 1
        else:
            dp[s2_plus_idx][s1_plus_idx] = max(dp[s2_plus_idx][s1_plus_idx - 1], dp[s2_plus_idx - 1][s1_plus_idx])

print(dp[len(sentence2)][len(sentence1)])
