X = int(input())
dp = [0 for _ in range(X + 1)]
path_dp = [0 for _ in range(X + 1)]
for target in range(2, X + 1):
    dp[target] = dp[target - 1] + 1
    path_dp[target] = target - 1
    if target % 2 == 0 and dp[target // 2] < dp[target]:
        dp[target] = dp[target//2] + 1
        path_dp[target] = target//2
    if target % 3 == 0 and dp[target // 3] < dp[target]:
        dp[target] = dp[target//3] + 1
        path_dp[target] = target//3

print(dp[X])
path_result = [str(X)]
path_track = X
while path_track > 1:
    path_result.append(str(path_dp[path_track]))
    path_track = path_dp[path_track]
print(' '.join(path_result))