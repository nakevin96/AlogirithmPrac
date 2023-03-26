# 자두나무 : https://www.acmicpc.net/problem/2240
# 매초 두 나무 중 하나에서 자두가 떨어짐.
# 해당 나무 아래 서있으면 그 열매를 먹을 수 있음
# 자두가 T초 동안 떨어질 때 자두는 최대 W만큼만 움직이고 싶음
# 매초 어느 나무에서 자두가 떨어지는지 알 수 있을 때 자두가 받을 수 있는 자두의 갯수를 구하라
import sys

input = sys.stdin.readline
T, W = map(int, input().split(' '))
# row: 몇번 바꾸는지 / col: 떨어진 시간
dp = [[0 for _ in range(T + 1)] for _ in range(W + 1)]
tree_list = [0 for _ in range(T + 1)]
for t in range(1, T + 1):
    tree = int(input())
    tree_list[t] = tree
    if tree == 1:
        dp[0][t] = dp[0][t - 1] + 1
    else:
        dp[0][t] = dp[0][t - 1]

for w in range(1, W + 1):
    for t in range(1, T + 1):
        dp[w][t] = max(dp[w - 1][t - 1], dp[w][t - 1])
        # 홀 수번 옮기면 짝수 나무 아래 위치
        if w % 2 == 1 and tree_list[t] == 2:
            dp[w][t] += 1
        elif w % 2 == 0 and tree_list[t] == 1:
            dp[w][t] += 1

result = 0
for w in range(W + 1):
    result = max(result, dp[w][T])
print(result)
